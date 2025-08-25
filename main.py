from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.embedding import Embedder
from app.retriever import Retriever
from app.generator import Generator

import numpy as np

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for Docker networking
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

embedder = Embedder()
retriever = Retriever()
retriever.load_index()
generator = Generator()

# Load raw documents
with open("data/sample.txt", "r", encoding="utf-8") as f:
    docs = f.readlines()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):
    q_embed = embedder.get_embeddings([query.question])
    q_embed = np.array(q_embed).astype("float32")

    indices, distances = retriever.search(q_embed, k=1)

    # safety check
    if len(indices) == 0 or distances[0] > 0.7:   # adjust threshold
        return {
            "question": query.question,
            "answer": "Sorry, I don't have information about that.",
            "context": ""
        }

    context = docs[indices[0]].strip()
    answer = generator.generate_answer(context, query.question)

    return {"question": query.question, "answer": answer.strip(), "context": context}
