import os
import tempfile
import streamlit as st
from langchain.chains import RetrievalQA
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from PyPDF2 import PdfReader
from langchain.schema import Document

# Defining the create_retrieval_qa function
def create_retrieval_qa(vectordb):
    # Initialize Ollama language model
    llm = Ollama(base_url='http://localhost:11434')  # Remove model_name

    # Create the QA chain with the vector store and LLM
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectordb.as_retriever(),
        return_source_documents=True
    )
    return qa_chain

def process_pdf(pdf_path, chunk_size=1000):
    reader = PdfReader(pdf_path)
    texts = []
    for page in reader.pages:
        text = page.extract_text() or ""
        # Chunk the text into smaller pieces and wrap each chunk in a Document
        texts.extend([Document(page_content=text[i:i+chunk_size]) for i in range(0, len(text), chunk_size)])
    return texts

st.title("Chat with PDF")
st.caption("This app allows you to chat with a PDF using Ollama models and Chroma for vector storage!")

# Initialize embeddings
embeddings = OllamaEmbeddings(base_url='http://localhost:11434')

# Create a temporary directory to store the PDF file
db_path = tempfile.mkdtemp()

# Upload a PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

# Initialize Chroma vector store and QA chain
vectordb = None
qa_chain = None

# If a PDF file is uploaded, process it and add it to the knowledge base
if pdf_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(pdf_file.getvalue())
        f.close()
        
        # Process the PDF and get a list of Document objects
        documents = process_pdf(f.name)
        
        # Create the Chroma vector store with processed documents
        vectordb = Chroma.from_documents(documents, embeddings, persist_directory=db_path)
        
        # Create the QA chain with the vector store
        qa_chain = create_retrieval_qa(vectordb)
        
    st.success(f"Added {pdf_file.name} to knowledge base!")

# Ask a question about the PDF
prompt = st.text_input("Ask a question about the PDF")

# Display the answer
if prompt and qa_chain:
    result = qa_chain.invoke({"query": prompt})
    answer = result.get('result')
    st.write(answer)
