import streamlit as st

from core.config import llm
from core.rag import load_vector_store
from core.embeddings import embedding_model

st.title("✍️ Research Writer")

st.write("Generate academic content from your uploaded research papers.")

topic = st.text_input("Research Topic")

output_type = st.selectbox(
    "Choose Output",
    [
        "Abstract",
        "Literature Review",
        "Methodology",
        "Results Summary",
        "Conclusion",
        "Future Work"
    ]
)

if st.button("Generate"):

    db = load_vector_store(embedding_model)

    retriever = db.as_retriever(search_kwargs={"k":8})

    docs = retriever.invoke(topic)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are an academic research assistant.

Using ONLY the information below,

write a professional {output_type}.

Topic:
{topic}

Research Papers:

{context}

Write in academic language.
"""

    with st.spinner("Generating..."):

        answer = llm.invoke(prompt).content

    st.success("Done!")

    st.markdown(answer)

    st.download_button(
       "📥 Download Report",
       answer,
       file_name=f"{output_type}.md"
    )

st.divider()

st.caption(
    "InsightAI • Agentic Research Assistant • Built with LangGraph, LangChain, FAISS, Groq and Streamlit"
)    