from sentence_transformers import SentenceTransformer
import numpy as np
from config import Config

class EmbeddingTool:
    def __init__(self):
        self.model = SentenceTransformer(Config.EMBEDDING_MODEL)
    
    def embed_text(self, text: str) -> np.ndarray:
        vec = self.model.encode([text])[0]
        return vec
