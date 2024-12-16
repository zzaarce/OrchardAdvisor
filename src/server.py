from flask import Flask, request, jsonify
from rag_pipeline import RAGPipeline

app = Flask(__name__)

# 初始化RAGPipeline实例
pipeline = RAGPipeline()

@app.route("/api/answer", methods=["POST"])
def answer():
    """
    接收JSON请求，参数示例：
    {
      "query": "最新的iPhone有哪些特性？"
    }
    返回JSON响应：
    {
      "question": "最新的iPhone有哪些特性？",
      "answer": "..."
    }
    """
    data = request.get_json()
    if not data or "query" not in data:
        return jsonify({"error": "Missing 'query' in request"}), 400
    
    query = data["query"]
    answer = pipeline.answer_query(query)
    return jsonify({"question": query, "answer": answer})

if __name__ == "__main__":
    # 默认在localhost:5000启动服务
    app.run(host="0.0.0.0", port=5000, debug=False)
