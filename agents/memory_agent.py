from langchain_core.messages import AIMessage

def memory_agent(state):

    name = state.get("customer_name")

    issue = state.get("issue_type")

    if name:
        reply = f"Your name is {name}. Your previous support issue was related to {issue}."
    else:
        reply = "I couldn't find any previous customer information."

    return {
        **state,
        "response": reply,
        "messages": [
            AIMessage(content=reply)
        ]
    }