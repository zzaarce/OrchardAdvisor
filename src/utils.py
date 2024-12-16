import pandas as pd
from config import Config

def load_documents():
    # 假定无表头，每行一个文本片段
    df = pd.read_csv(Config.DOCS_CSV_PATH, header=None, names=["text"])
    doc_map = {idx: row["text"] for idx, row in df.iterrows()}
    docs = list(doc_map.values())
    return docs, doc_map
