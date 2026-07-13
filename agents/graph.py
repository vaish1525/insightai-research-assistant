from langgraph.graph import StateGraph, END

from agents.state import AgentState
from agents.nodes import (
    router_node,
    rag_node,
    web_node,
    both_node
)

workflow = StateGraph(AgentState)

workflow.add_node("router", router_node)
workflow.add_node("rag", rag_node)
workflow.add_node("web", web_node)
workflow.add_node("both", both_node)

workflow.set_entry_point("router")


def decide(state):

    return state["route"].lower()


workflow.add_conditional_edges(
    "router",
    decide,
    {
        "rag": "rag",
        "web": "web",
        "both": "both"
    }
)

workflow.add_edge("rag", END)
workflow.add_edge("web", END)
workflow.add_edge("both", END)

graph = workflow.compile()