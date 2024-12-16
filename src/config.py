class Config:
    # 大模型API的配置（此处以OpenAI为例）
    MODEL_API_KEY = "YOUR_LLM_API_KEY"
    MODEL_ENDPOINT = "https://api.openai.com/v1/chat/completions"
    MODEL_NAME = "gpt-3.5-turbo"  # 可根据权限与需求更改

    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    INDEX_PATH = "./data/embeddings/index.faiss"
    DOCS_CSV_PATH = "./data/documents/documents.csv"  # 文本切片CSV文件路径
    RETRIEVAL_TOP_K = 3
