from core.pdf_loader import save_uploaded_files, load_documents
from core.text_splitter import split_documents
from core.embeddings import embedding_model
from core.rag import create_vector_store


def process_documents(uploaded_files):

    file_paths = save_uploaded_files(uploaded_files)

    docs = load_documents(file_paths)

    chunks = split_documents(docs)

    db = create_vector_store(
        chunks,
        embedding_model
    )

    return len(docs), len(chunks)