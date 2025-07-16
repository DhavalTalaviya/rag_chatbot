# RAG Chatbot Demo 🤖📚

A Retrieval-Augmented Generation (RAG) chatbot built with:
- 🧠 LangChain
- 🔗 FAISS
- 💬 Ollama (local LLM, e.g., Gemma3, LLaMA3)
- 🌐 Streamlit frontend

## 🚀 Features

✅ Ask questions about a local PDF  
✅ Retrieve relevant chunks using FAISS  
✅ Answer via local LLM (no OpenAI API needed)  
✅ Streamlit web interface

## 🛠 Setup

1️⃣ Clone the repo:
```bash
git clone https://github.com/yourusername/rag_chatbot.git
cd rag_chatbot

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Start Ollama and pull model (if not done):

ollama pull llama3
ollama run llama3

4️⃣ Run the app:

streamlit run app.py