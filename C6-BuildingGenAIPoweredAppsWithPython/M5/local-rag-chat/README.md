# Local PDF Chat (RAG) with Llama 3 & Ollama

This is a 100% local and free Retrieval-Augmented Generation (RAG) application. It allows users to upload PDF documents and have a conversation with the content using the Llama 3 model running locally via Ollama. No data leaves your machine, ensuring complete privacy and security.

## Features
- **100% Local:** All processing, from PDF parsing to LLM generation, happens on your hardware.
- **Privacy First:** Your documents and chat history are never sent to the cloud.
- **Zero Cost:** No API keys or subscriptions required.
- **Modern RAG Stack:** Built using LangChain, Ollama, ChromaDB, and Flask.

## Prerequisites
- [Python 3.10+](https://www.python.org/)
- [Ollama](https://ollama.com/) installed and running.
- Llama 3 model pulled in Ollama:
  ```bash
  ollama pull llama3
  ```

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd local-rag-chat
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   .\\venv\\Scripts\\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask langchain-ollama langchain-huggingface chromadb pypdf sentence-transformers
   ```

## Project Structure
```text
local-rag-chat/
├── static/
│   └── uploads/      # Uploaded PDF storage
├── templates/
│   └── index.html    # Web UI
├── chroma_db/        # Local vector database (created at runtime)
├── server.py         # Flask backend
├── worker.py         # AI and RAG logic
└── README.md
```

## Usage

1. **Start the Flask server:**
   ```bash
   python server.py
   ```

2. **Access the Web UI:**
   Open your browser and navigate to `http://127.0.0.1:8000`.

3. **Chatting with your PDF:**
   - Click **Choose File** to select a PDF.
   - Click **Upload PDF** and wait for the "Done!" status.
   - Type your questions in the chat box and hit **Send**.

## Technology Stack
- **LLM:** Llama 3 (via Ollama)
- **Orchestration:** LangChain
- **Embeddings:** HuggingFace `all-MiniLM-L6-v2` (Local)
- **Vector Store:** ChromaDB
- **Backend:** Flask
- **Frontend:** HTML/CSS/JavaScript
