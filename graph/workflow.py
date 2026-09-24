from langgraph.graph import StateGraph, START, END

from graph.state import AgentState
from agents.supervisor import supervisor
from agents.search_agent import search_agent as real_search_agent
from agents.synthesis_agent import synthesis_agent


# ============================================================
# SEARCH AGENT
# ============================================================

def search_node(state: AgentState):
    """
    Connect LangGraph with the real RAG Search Agent.
    """

    print("Search Agent selected")

    question = state["question"]

    result = real_search_agent(
        question,
        top_k=5
    )

    return {
        "search_results": [
            result["answer"]
        ]
    }


# ============================================================
# VISION AGENT
# ============================================================

def vision_agent(state: AgentState):
    """
    Temporary Vision Agent.
    """

    print("Vision Agent selected")

    return {
        "vision_results": [
            "Vision Agent received the question."
        ]
    }


# ============================================================
# SQL AGENT
# ============================================================

def sql_agent(state: AgentState):
    """
    Temporary SQL Agent.
    """

    print("SQL Agent selected")

    return {
        "sql_results": [
            "SQL Agent received the question."
        ]
    }


# ============================================================
# MULTI AGENT
# ============================================================

def multi_agent(state: AgentState):
    """
    Execute multiple agents when required.
    """

    print("Multiple agents required")

    # Search Agent
    search_result = real_search_agent(
        state["question"],
        top_k=5
    )

    # SQL Agent
    sql_result = sql_agent(state)

    return {
        "search_results": [
            search_result["answer"]
        ],
        "sql_results": sql_result["sql_results"]
    }


# ============================================================
# CREATE LANGGRAPH
# ============================================================

builder = StateGraph(AgentState)


# Add nodes
builder.add_node(
    "supervisor",
    supervisor
)

builder.add_node(
    "search",
    search_node
)

builder.add_node(
    "vision",
    vision_agent
)

builder.add_node(
    "sql",
    sql_agent
)

builder.add_node(
    "multi",
    multi_agent
)

builder.add_node(
    "synthesis",
    synthesis_agent
)


# ============================================================
# START → SUPERVISOR
# ============================================================

builder.add_edge(
    START,
    "supervisor"
)


# ============================================================
# SUPERVISOR ROUTING
# ============================================================

def route_question(state: AgentState):

    return state["next_agent"]


builder.add_conditional_edges(
    "supervisor",
    route_question,
    {
        "search": "search",
        "vision": "vision",
        "sql": "sql",
        "multi": "multi"
    }
)


# ============================================================
# AGENTS → SYNTHESIS
# ============================================================

builder.add_edge(
    "search",
    "synthesis"
)

builder.add_edge(
    "vision",
    "synthesis"
)

builder.add_edge(
    "sql",
    "synthesis"
)

builder.add_edge(
    "multi",
    "synthesis"
)


# ============================================================
# SYNTHESIS → END
# ============================================================

builder.add_edge(
    "synthesis",
    END
)


# ============================================================
# COMPILE GRAPH
# ============================================================

graph = builder.compile()