from graph.workflow import build_graph
from langchain_core.messages import HumanMessage

graph = build_graph()

print("=" * 55)
print(" AI-Powered Customer Support Automation System ")
print("=" * 55)

thread_id = input(
    "Customer Session ID: "
).strip() or "customer_001"

config = {
    "configurable": {
        "thread_id": thread_id
    }
}

while True:

    query = input("\nCustomer: ")

    if query.lower() == "quit":
        break

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=query)
            ]
        },
        config=config
    )
    print(
        "\nSupport:",
        result["messages"][-1].content
    )