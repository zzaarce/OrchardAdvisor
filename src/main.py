from rag_pipeline import RAGPipeline

if __name__ == "__main__":
    pipeline = RAGPipeline()
    user_query = "最新的iPhone有哪些特性？"
    answer = pipeline.answer_query(user_query)
    print("用户问题：", user_query)
    print("系统回答：", answer)
