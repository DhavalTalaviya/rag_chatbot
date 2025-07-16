import streamlit as st
from dotenv import load_dotenv
from chat import create_qa_chain, ask_question

# Load environment variables
load_dotenv()

# Streamlit app title and description
st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("📚 Ask Your PDF - RAG Chatbot")
st.markdown("Upload a PDF, ask any question, and get smart answers from your document!")

# Load the QA chain only once (cached)
@st.cache_resource
def load_chain():
    return create_qa_chain()

qa_chain = load_chain()

# User input for questions
question = st.text_input("💬 **Your Question**", placeholder="Type your question about the document...")

if question:
    with st.spinner("🤔 Thinking..."):
        try:
            response = ask_question(qa_chain, question)
            st.write("🤖 **Answer:**", response)
        except Exception as e:
            st.error(f"Error: {e}")
