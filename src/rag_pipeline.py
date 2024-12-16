from config import Config
from llm_interface import LLMInterface
from embedding_tool import EmbeddingTool
from search_tool import VectorRetriever

class RAGPipeline:
    def __init__(self):
        self.llm = LLMInterface()
        self.embed_tool = EmbeddingTool()
        self.retriever = VectorRetriever()

    def answer_query(self, query: str, context_messages=None):
        if context_messages is None:
            context_messages = []

        q_emb = self.embed_tool.embed_text(query).reshape(1, -1)
        docs = self.retriever.search(q_emb, top_k=Config.RETRIEVAL_TOP_K)
        retrieved_text = "\n\n".join([f"{i+1}. {d[0]}" for i, d in enumerate(docs)])

        messages = context_messages + [
            {"role": "system", "content": "你是一个苹果产品售前智能问答助手。请基于下列文档信息回答用户问题。"},
            {"role": "system", "content": f"检索到的文档信息：\n{retrieved_text}\n"},
            {"role": "user", "content": query}
        ]

        answer = self.llm.chat(messages)
        return answer
