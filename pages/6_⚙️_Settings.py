import streamlit as st
import os

st.title("⚙️ Settings")

st.success("AI Status: Connected")

st.write("Current Model")

st.code(os.getenv("MODEL_NAME"))

st.write("Embedding Model")

st.code("BAAI/bge-small-en-v1.5")

st.write("Vector Database")

st.code("FAISS")

st.write("Framework")

st.code("LangGraph + LangChain")

st.write("LLM Provider")

st.code("Groq")