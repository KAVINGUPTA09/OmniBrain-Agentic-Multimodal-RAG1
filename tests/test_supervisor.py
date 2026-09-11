from graph.workflow import graph


def test_question(question):
    result = graph.invoke({
        "question": question,
        "next_agent": "",
        "search_results": [],
        "vision_results": [],
        "sql_results": [],
        "final_answer": ""
    })

    print("\nQuestion:", question)

    if result["search_results"]:
        print("Agent: SEARCH")

    elif result["vision_results"]:
        print("Agent: VISION")

    elif result["sql_results"]:
        print("Agent: SQL")


# Test 1
test_question("What was the company's revenue?")


# Test 2
test_question("What does the revenue chart show?")


# Test 3
test_question("What was the stock price?")