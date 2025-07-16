import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from ingest import ingest_pdf  # import the function from ingest.py

def load_vectorstore(path="data/vector_store"):
    # Check if the FAISS index file exists
    if not os.path.exists(f"{path}/index.faiss"):
        print("⚠️ Vector store not found. Running ingestion...")
        ingest_pdf()  # Run ingestion automatically

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
