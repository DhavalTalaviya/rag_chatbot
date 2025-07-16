from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama
from vector_store import load_vectorstore

def create_qa_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    
    llm = ChatOllama(model="llama3")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

def ask_question(chain, question):
    response = chain(question)
    return response["result"]