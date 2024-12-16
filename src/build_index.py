import faiss
import numpy as np
import os
from config import Config
from utils import load_documents
from embedding_tool import EmbeddingTool

def build_index():
    if not os.path.exists("./data/embeddings"):
        os.makedirs("./data/embeddings")
    
    docs, doc_map = load_documents()
    embed_tool = EmbeddingTool()

    vectors = []
    for doc in docs:
        vec = embed_tool.embed_text(doc)
        vectors.append(vec)
    vectors = np.array(vectors).astype('float32')
    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)
    faiss.write_index(index, Config.INDEX_PATH)
    print("Index built and saved to:", Config.INDEX_PATH)

if __name__ == "__main__":
    build_index()
