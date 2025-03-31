# Imports Here
import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain_groq import ChatGroq

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not MISTRAL_API_KEY and not GROQ_API_KEY:
    raise ValueError("API keys are missing. Please set them in the environment variables.")

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

def get_vector_store(text_chunks):
        embeddings = MistralAIEmbeddings(
        model="mistral-embed",
    )
        vectorstore = FAISS.from_texts(text_chunks, embedding = embeddings)
        return vectorstore

def get_conversation_chain(vectorStore):
    llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,
    max_retries=2,
)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
    )
    conversation_chain =  ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vectorStore.as_retriever(),
        memory = memory,
    )

    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate (st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}" , message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}" , message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    # Title
    st.set_page_config(page_title="Chat With Multiple PDFs", page_icon="📄")
    
    # Adding CSS on the top
    st.write(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
        
    st.header("DocuMind : Chat With Multiple PDFs  :books:")
    user_question = st.text_input("Ask me anything about PDFs")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your PDFs")
        pdf_docs = st.file_uploader(
            "Upload your PDFs", accept_multiple_files=True)

        if st.button("PROCESS"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF file.")
                return

            with st.spinner("Processing..."):
                # get PDF text
                raw_text = get_pdf_text(pdf_docs)
                # st.write(raw_text)

                # get text chunks
                text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks)

                # create vector store
                vectorStore = get_vector_store(text_chunks)
                
                # Create Conversation Chain
                st.session_state.conversation = get_conversation_chain(vectorStore)


if __name__ == '__main__':
    main()