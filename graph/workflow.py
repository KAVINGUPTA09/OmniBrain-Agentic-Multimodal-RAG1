from langgraph.graph import StateGraph, START, END

from graph.state import AgentState
from agents.supervisor import supervisor


# -----------------------------
# Test Search Agent
# -----------------------------
def search_agent(state: AgentState):
    print("Search Agent selected")

    return {
        "search_results": ["Search Agent received the question."]
    }


# -----------------------------
# Test Vision Agent
# -----------------------------
def vision_agent(state: AgentState):
    print("Vision Agent selected")

    return {
        "vision_results": ["Vision Agent received the question."]
    }


# -----------------------------
# Test SQL Agent
# -----------------------------
def sql_agent(state: AgentState):
    print("SQL Agent selected")

    return {
        "sql_results": ["SQL Agent received the question."]
    }


# -----------------------------
# Create LangGraph
# -----------------------------
builder = StateGraph(AgentState)

# Add nodes
builder.add_node("supervisor", supervisor)
builder.add_node("search", search_agent)
builder.add_node("vision", vision_agent)
builder.add_node("sql", sql_agent)

# Start → Supervisor
builder.add_edge(START, "supervisor")


# -----------------------------
# Routing function
# -----------------------------
def route_question(state: AgentState):
    return state["next_agent"]


# Supervisor → Selected Agent
builder.add_conditional_edges(
    "supervisor",
    route_question,
    {
        "search": "search",
        "vision": "vision",
        "sql": "sql",
    },
)


# Agents → End
builder.add_edge("search", END)
builder.add_edge("vision", END)
builder.add_edge("sql", END)


# Compile the graph
graph = builder.compile()