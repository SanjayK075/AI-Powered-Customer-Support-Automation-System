from knowledge_base.pricing_guide import PRICING_KB
from knowledge_base.technical_manual import TECHNICAL_KB
from knowledge_base.company_policy import POLICY_KB
from knowledge_base.faq import FAQ_KB


def rag_node(state):
    query = state["messages"][-1].content.lower()

    context = ""

    if state["issue_type"] == "sales":
        for key, value in PRICING_KB.items():
            if key in query:
                context += value + "\n"

    elif state["issue_type"] == "technical":
        for key, value in TECHNICAL_KB.items():
            if key in query:
                context += value + "\n"

    elif state["issue_type"] == "billing":
        for key, value in POLICY_KB.items():
            if key in query:
                context += value + "\n"

    elif state["issue_type"] == "account":
        for key, value in FAQ_KB.items():
            if key in query:
                context += value + "\n"

    if context == "":
        context = "No relevant information found."

    state["retrieved_context"] = context

    return state