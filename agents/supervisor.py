from graph.state import AgentState


def supervisor(state: AgentState):
    question = state["question"].lower()

    # Stock-related questions → SQL Agent
    if "stock" in question or "share price" in question:
        next_agent = "sql"

    # Chart/image/table-related questions → Vision Agent
    elif (
        "chart" in question
        or "graph" in question
        or "image" in question
        or "table" in question
    ):
        next_agent = "vision"

    # Other questions → Search Agent
    else:
        next_agent = "search"

    return {
        "next_agent": next_agent
    }