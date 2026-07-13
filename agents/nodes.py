from core.config import llm
from core.embeddings import embedding_model
from core.rag import ask_question
from core.search_tool import search_web
from duckduckgo_search import DDGS

ROUTER_PROMPT = """
You are an AI router.

Choose ONLY ONE option.

RAG
WEB
BOTH

Rules:

- If the answer should come from uploaded PDFs → RAG
- If it requires recent/current/latest/live information → WEB
- If both uploaded documents and recent information are useful → BOTH

Question:
{question}

Return ONLY one word.
"""


def router_node(state):

    question = state["question"].lower()

    # Current information
    if any(word in question for word in [
        "latest",
        "today",
        "current",
        "news",
        "recent",
        "2025",
        "2026",
        "ceo",
        "price",
        "stock",
        "release",
        "launch"
    ]):
        state["route"] = "WEB"

    # Uploaded paper questions
    elif any(word in question for word in [
        "paper",
        "document",
        "method",
        "dataset",
        "algorithm",
        "author",
        "figure",
        "table",
        "section",
        "summarize",
        "conclusion"
    ]):
        state["route"] = "RAG"

    else:
        state["route"] = "BOTH"

    return state

def rag_node(state):

    answer, docs = ask_question(
        state["question"],
        embedding_model
    )

    state["answer"] = answer
    state["docs"] = docs

    return state

def web_node(state):
    question = state["question"]

    with DDGS() as ddgs:
        results = list(ddgs.text(question, max_results=5))

    context = ""

    for result in results:
        context += f"Title: {result['title']}\n"
        context += f"Content: {result['body']}\n\n"

    prompt = f"""
You are InsightAI.

Using the following web search results, answer the user's question clearly.

Question:
{question}

Search Results:
{context}

Provide a concise answer.
"""

    answer = llm.invoke(prompt).content

    state["answer"] = answer
    state["docs"] = []

    return state

def both_node(state):

    rag_answer, docs = ask_question(
        state["question"],
        embedding_model
    )

    web_results = search_web(state["question"])

    web_context = ""

    for r in web_results:

        web_context += r["body"] + "\n"

    final_prompt = f"""
You are InsightAI.

Combine these two sources into one answer.

DOCUMENT INFORMATION:

{rag_answer}

WEB INFORMATION:

{web_context}

Question:

{state["question"]}

Generate one final answer.
"""

    answer = llm.invoke(final_prompt).content

    state["answer"] = answer
    state["docs"] = docs

    return state