from typing import TypedDict


class AgentState(TypedDict):

    question: str
    next_agent: str
    selected_agents: list
    search_results: list
    vision_results: list
    sql_results: list
    final_answer: str