from graph.workflow import graph


def test_question(question):

    result = graph.invoke({
        "question": question,
        "next_agent": "",
        "selected_agents": [],
        "search_results": [],
        "vision_results": [],
        "sql_results": [],
        "final_answer": ""
    })

    print("\n" + "=" * 60)
    print("Question:", question)
    print("Selected agents:", result["selected_agents"])
    print("Final Answer:")
    print(result["final_answer"])


# -----------------------------
# Test 1: Search
# -----------------------------
test_question(
    "What was the company's revenue?"
)


# -----------------------------
# Test 2: Vision
# -----------------------------
test_question(
    "What does the revenue chart show?"
)


# -----------------------------
# Test 3: SQL
# -----------------------------
test_question(
    "What was the stock price?"
)


# -----------------------------
# Test 4: Multiple Agents
# -----------------------------
test_question(
    "Compare the company's revenue with its stock performance."
)