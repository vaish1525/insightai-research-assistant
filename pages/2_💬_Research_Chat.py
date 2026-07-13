import streamlit as st


from agents.graph import graph

st.title("💬 Research Chat")
st.caption(
    "Ask questions about uploaded research papers or current research topics. "
    "The LangGraph agent automatically decides whether to use PDFs, the web, or both."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask anything about your research papers...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.status("🧠 Thinking...", expanded=True) as status:

        st.write("📚 Searching document database...")
        st.write("🔍 Retrieving relevant sections...")
        st.write("🤖 Generating response...")

       

        try:

            result = graph.invoke(
               {
                    "question": question,
                    "route": "",
                    "answer": "",
                    "docs": []
                }
            )

            route = result["route"]
            answer = result["answer"]
            docs = result["docs"]

            st.success(f"🧠 LangGraph selected: {route}")

        except Exception as e:

            st.error("⚠️ The AI model is temporarily unavailable. Please try again in a few seconds.")

            st.exception(e)

            st.stop()

        status.update(
            label=f"✅ Answer Generated ({route})",
            state="complete"
        )

    with st.chat_message("assistant"):

        if route == "RAG":
            st.caption("🧠 LangGraph Route: 📚 Document Retrieval (RAG)")

        elif route == "WEB":
            st.caption("🧠 LangGraph Route: 🌐 Web Search")

        else:
            st.caption("🧠 LangGraph Route: 🔀 Hybrid")


        placeholder = st.empty()

        text = ""

        for word in answer.split():
            text += word + " "
            placeholder.markdown(text + "▌")

        placeholder.markdown(text)
        if docs:

            with st.expander("📚 Sources"):

                for doc in docs:

                    page = doc.metadata.get("page", "?")
                    source = doc.metadata.get("source", "Unknown")

                    st.write(f"📄 {source} — Page {page+1}")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        st.download_button(
            "⬇ Download Answer",
            answer,
            file_name="answer.txt"
        )

    with c2:
        st.button("👍 Helpful")

st.divider()

st.caption(
    "InsightAI • Agentic Research Assistant • Built with LangGraph, LangChain, FAISS, Groq and Streamlit"
)        