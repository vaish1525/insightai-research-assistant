import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

DOCUMENTS_DIR = "data/documents"

Path(DOCUMENTS_DIR).mkdir(parents=True, exist_ok=True)


def save_uploaded_files(uploaded_files):
    saved_paths = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join(DOCUMENTS_DIR, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        saved_paths.append(file_path)

    return saved_paths


def load_documents(file_paths):
    documents = []

    for path in file_paths:
        loader = PyPDFLoader(path)
        docs = loader.load()
        documents.extend(docs)

    return documents