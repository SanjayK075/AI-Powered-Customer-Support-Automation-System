from langchain_core.messages import AIMessage
from utils.llm import llm
from knowledge_base.company_policy import POLICY_KB

def billing_agent(state):

    question = state["messages"][-1].content

    context = state["retrieved_context"]

    if context == "No relevant information found.":
        context = "\n".join(POLICY_KB.values())

    result = llm.invoke(
        f"""
You are a Billing Support Executive for ABC Technologies.

Context:
{context}

Customer Question:
{question}

Answer the customer's question professionally using the given context.
"""
    )

    return {
        **state,
        "response": result.content,
        "messages": [
            AIMessage(content=result.content)
        ]
    }