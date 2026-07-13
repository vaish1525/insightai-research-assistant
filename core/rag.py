from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

from core.config import llm
from core.prompts import RAG_PROMPT

VECTOR_DB = "vector_store/faiss_index"


def create_vector_store(chunks, embedding_model):

    db = FAISS.from_documents(
        chunks,
        embedding_model
    )

    Path("vector_store").mkdir(exist_ok=True)

    db.save_local(VECTOR_DB)

    return db


def load_vector_store(embedding_model):

    return FAISS.load_local(
        VECTOR_DB,
        embedding_model,
        allow_dangerous_deserialization=True
    )


def ask_question(question, embedding_model):

    db = load_vector_store(embedding_model)

    retriever = db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 8
        }
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = PromptTemplate.from_template(RAG_PROMPT)

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content, docs