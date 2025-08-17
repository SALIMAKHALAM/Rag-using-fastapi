from fastapi import FastAPI
from pydantic import BaseModel
from app.embedding import Embedder
from app.retriever import Retriever
from app.generator import Generator

import numpy as np

app = FastAPI()
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

    top_k_idxs = retriever.search(q_embed, k=3)
    context = "\n".join([docs[i].strip() for i in top_k_idxs])
    answer = generator.generate_answer(context, query.question)

    return {"question": query.question, "answer": answer.strip(), "context": context}
