import faiss
import numpy as np
from config import Config
from utils import load_documents

class VectorRetriever:
    def __init__(self):
        self.index = faiss.read_index(Config.INDEX_PATH)
        _, self.doc_map = load_documents()

    def search(self, query_embedding: np.ndarray, top_k=3):
        D, I = self.index.search(query_embedding, top_k)
        results = []
        for i, score in zip(I[0], D[0]):
            doc = self.doc_map[i]
            results.append((doc, score))
        return results
