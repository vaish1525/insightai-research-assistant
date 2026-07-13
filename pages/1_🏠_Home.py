import streamlit as st

st.title("🧠 InsightAI")

st.subheader("Agentic AI Research Assistant")

st.markdown("""
Welcome to **InsightAI** — an AI-powered research platform built using **LangGraph, RAG, FAISS and LLMs**.

This assistant can understand research papers, search the web, generate literature reviews and help researchers work much faster.
""")

import os

folder = "data/documents"

pdfs = len([f for f in os.listdir(folder) if f.endswith(".pdf")])

chunks = 0

if os.path.exists("vector_store/faiss_index"):
    chunks = "Ready"

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Papers", pdfs)

with col2:
    st.metric("🗂 Vector DB", chunks)

with col3:
    st.metric("🤖 AI Agent", "Online")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AI Agent", "Ready ✅")

with col2:
    st.metric("Vector Database", "Connected ✅")

with col3:
    st.metric("Research Mode", "Active ✅")

st.divider()

st.subheader("🚀 Features")

c1, c2 = st.columns(2)

with c1:

    st.success("""
📄 Chat with Research Papers

Ask questions from uploaded PDFs using Retrieval Augmented Generation (RAG).
""")

    st.success("""
🧠 LangGraph AI Agent

Automatically decides whether to use uploaded documents, web search, or both.
""")

    st.success("""
📚 Literature Review Generator

Generate literature reviews, summaries and research notes instantly.
""")

with c2:


    st.success("""
📖 Research Library

Upload and manage multiple research papers.
""")

    st.success("""
⚡ Powered by Groq

Ultra-fast LLM inference with open-source models.
""")

st.divider()

st.info(
"""
### 🛠 Tech Stack

• LangGraph

• LangChain

• FAISS

• Sentence Transformers

• Groq API

• Streamlit

• DuckDuckGo Search

• Python
"""
)

st.divider()

st.caption(
    "InsightAI • Agentic Research Assistant • Built with LangGraph, LangChain, FAISS, Groq and Streamlit"
)