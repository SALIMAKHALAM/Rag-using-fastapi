Retrieval-Augmented Generation (RAG) API 🚀

A FastAPI-based Retrieval-Augmented Generation (RAG) system that combines ChromaDB (vector database) and FLAN-T5 (LLM) to deliver context-aware answers from custom documents.

✨ Features:

🔍 Semantic Search: Embedding-based retrieval using MiniLM.
⚡ Ultra-Fast Retrieval: Achieved ~2.4 ms average retrieval latency.
⏱️ Optimized Response Time: End-to-end query answering in ~2.42 s on CPU.
📦 Vector Store: ChromaDB for persistent document storage and retrieval.
🧠 LLM Response Generation: Context-aware answer generation using FLAN-T5.
🌐 API Ready: FastAPI endpoints for uploading documents and querying.

Installation:

1.Clone the repo:

git clone https://github.com/your-username/rag-api-framework.git
cd rag-api-framework


2.Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


3.Install dependencies:

pip install -r requirements.txt

4.Running the API

Start the FastAPI server:
uvicorn app.main:app --reload


5.Visit the interactive Swagger UI:

http://127.0.0.1:8000/docs


Available endpoints:

POST /upload → Upload and index documents into ChromaDB
POST /query → Ask a question and get context-aware answers

📊 Evaluation:

Retrieval Latency (ChromaDB): ~2.4 ms (CPU)
End-to-End Query Time (Retrieval + FLAN-T5): ~2.42 s
Speedup: >100× faster than brute-force/manual lookup

🔮 Future Improvements:

GPU acceleration for lower end-to-end latency
Support for hybrid retrieval (BM25 + dense embeddings)
Streamed token generation for faster responses
