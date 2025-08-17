import os
from app.embedding import Embedder
from app.retriever import Retriever
import numpy as np

# Load documents
data_path = "data"
docs = []
file_names = []

for file in os.listdir(data_path):
    with open(os.path.join(data_path, file), "r", encoding="utf-8") as f:
        lines = f.readlines()
        docs.extend(lines)
        file_names.extend([file]*len(lines))

# Generate embeddings
embedder = Embedder()
embeddings = embedder.get_embeddings(docs)

# Save index
retriever = Retriever()
retriever.build_index(np.array(embeddings).astype("float32"))

print(f"Indexed {len(docs)} chunks from {len(set(file_names))} file(s).")

