from typing import TypedDict, List, Any


class AgentState(TypedDict):
    question: str
    route: str
    answer: str
    docs: List[Any]