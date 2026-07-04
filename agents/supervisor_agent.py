from langchain_core.messages import AIMessage
from utils.llm import llm

def supervisor_agent(state):

    response = state["response"]

    result = llm.invoke(
        f"""
You are a Customer Support Supervisor.

Review the following customer response.

Response:
{response}

If necessary, improve the wording while keeping the meaning unchanged.
"""
    )

    return {
        **state,
        "response": result.content,
        "messages": [
            AIMessage(content=result.content)
        ]
    }