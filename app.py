import streamlit as st

st.logo("https://raw.githubusercontent.com/streamlit/brand/main/logos/streamlit-mark-color.png")

st.sidebar.success("🟢 AI Connected")

st.sidebar.metric(
    "Knowledge Base",
    "Ready"
)

st.set_page_config(
    page_title="InsightAI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 InsightAI")
st.subheader("Your AI Research Workspace")

st.markdown("""
Welcome to **InsightAI**.

This application helps researchers, students and professionals to:

- 📄 Chat with multiple research papers
- 🤖 Perform Agentic AI powered research
- 🌐 Search the web when documents are insufficient
- ✍️ Generate literature reviews
- 📝 Generate summaries and notes
- 📚 Manage research libraries
- 📌 Get accurate citations

---

### 🚀 Current Version

Version **0.1 MVP**
""")

st.info("Select a module from the left sidebar.")

st.sidebar.title("🧠 InsightAI")

st.sidebar.markdown("---")

st.sidebar.success("✅ AI Connected")

st.sidebar.info("""
Features

📄 PDF Research Assistant

🧠 LangGraph Agent

📚 RAG + FAISS

🌐 Web Search

🤖 LLM Powered
""")