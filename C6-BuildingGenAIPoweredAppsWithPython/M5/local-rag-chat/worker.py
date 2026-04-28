import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQA

# Global variables to hold our local models
llm_hub = None
embeddings = None
vector_db = None

def init_llm():
    global llm_hub, embeddings
    # Connects to your local Ollama instance
    llm_hub = OllamaLLM(model="llama3")
    
    # Downloads a small embedding model (~80MB) to run locally on your CPU
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def process_document(document_path):
    global vector_db
    # 1. Load the PDF
    loader = PyPDFLoader(document_path)
    documents = loader.load()
    
    # 2. Split PDF into smaller chunks so the AI can read them
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    
    # 3. Create a local vector database in a folder named 'db'
    vector_db = Chroma.from_documents(
        documents=texts, 
        embedding=embeddings, 
        persist_directory="./chroma_db"
    )

def process_prompt(prompt):
    global vector_db, llm_hub
    
    # Check if a PDF has been uploaded yet
    if vector_db is None:
        return "Please upload a PDF document first so I have something to reference!"

    # Your existing chain logic...
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm_hub,
        chain_type="stuff",
        retriever=vector_db.as_retriever(search_kwargs={"k": 3})
    )
    result = qa_chain.invoke({"query": prompt})
    return result["result"]