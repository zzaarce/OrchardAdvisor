# OrchardAdvisor
### 作者
韩文强/中国传媒大学/hanwenqiang_qd@126.com
## 项目特性

- **检索增强生成（RAG）**：在回答用户查询前，先通过向量检索（FAISS）获取相关文本片段，提升回答的针对性和准确性。
- **数据灵活扩展**：使用 `documents.csv` 文件存储文本切片，每行一个片段，便于数据的添加、删除与更新。
- **灵活的大模型接入**：通过 `config.py` 配置 LLM 的 API Key、Endpoint 和模型名称，可轻松切换不同的模型服务（如 OpenAI）。
- **HTTP接口支持**：`server.py` 提供 REST API 接口，允许外部系统通过 JSON 请求进行调用，方便集成到现有业务流程中。

## 准备工作

### 1. 安装依赖

请确保已安装 Python 3.8+。然后在项目根目录下运行以下命令安装所需依赖：

```bash
pip install -r requirements.txt
```
### 2. 准备数据
在 `data/documents/documents.csv` 中添加文本片段数据，每行一个片段。例如：

```csv
iPhone 14是一款苹果智能手机，具备A系列芯片和优秀的摄像头性能。
Apple Watch具有健康监测、运动追踪和消息通知等功能。
苹果官方在线商店提供最新iPhone购买渠道和分期付款服务。
```

### 3. 配置大模型API
打开 src/config.py 文件，填写您的大模型API Key、Endpoint和模型名称。例如，使用 OpenAI API：
```bash
class Config:
    # 请将YOUR_LLM_API_KEY替换为您实际的LLM服务API Key
    MODEL_API_KEY = "YOUR_LLM_API_KEY"
    # OpenAI API的Endpoint
    MODEL_ENDPOINT = "https://api.openai.com/v1/chat/completions"
    MODEL_NAME = "gpt-3.5-turbo"  # 或 "gpt-4" 根据您的权限

    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    INDEX_PATH = "./data/embeddings/index.faiss"
    DOCS_CSV_PATH = "./data/documents/documents.csv"
    RETRIEVAL_TOP_K = 3
```
### 4. 构建向量索引
在项目根目录下运行以下命令，构建 FAISS 向量索引：
```bash
python src/build_index.py
```
此操作将对 documents.csv 中的文本进行向量化，并生成 index.faiss 索引文件。


## 使用说明
### 1.本地测试问答
运行 main.py 以测试问答功能：
```bash
python src/main.py
```
程序将调用大模型并检索结果回答示例查询，并在控制台输出结果。
### 2.通过HTTP接口访问
启动服务端接口：
```bash
python src/server.py
```
服务默认在 http://localhost:5000 运行。您可以通过以下方式访问 POST /api/answer 接口：
### 示例请求
```bash
curl -X POST http://localhost:5000/api/answer \
     -H "Content-Type: application/json" \
     -d '{"query": "最新的iPhone有哪些特性？"}'
```
#### 示例响应
```bash
{
  "question": "最新的iPhone有哪些特性？",
  "answer": "iPhone 16拥有更强的芯片性能和更好的摄像头表现..."
}
```





