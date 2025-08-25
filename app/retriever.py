import os
import faiss
import numpy as np

class Retriever:
    def __init__(self, index_path="indexes/index.faiss"):
        self.index_path = index_path
        self.index = None

    def build_index(self, embeddings):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

        os.makedirs("indexes", exist_ok=True)
        faiss.write_index(self.index, self.index_path)

    def load_index(self):
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
            return True
        return False

    def search(self, query_embedding, k=3):
        distances, indices = self.index.search(query_embedding, k)
        return indices[0], distances[0]   
