import streamlit as st

from core.pdf_loader import save_uploaded_files, load_documents
from core.text_splitter import split_documents
from core.embeddings import embedding_model
from core.rag import create_vector_store

st.title("📚 Research Library")

uploaded_files = st.file_uploader(
    "Upload Research Papers",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    saved_paths = save_uploaded_files(uploaded_files)

    docs = load_documents(saved_paths)

    chunks = split_documents(docs)

    create_vector_store(
        chunks,
        embedding_model
    )

    st.success("✅ Knowledge Base Created!")

    st.write(f"Pages Loaded: {len(docs)}")
    st.write(f"Chunks Created: {len(chunks)}")