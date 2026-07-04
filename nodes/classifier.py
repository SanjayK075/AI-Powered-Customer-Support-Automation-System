from graph.customer_state import CustomerState

def classify_query(state: CustomerState):
    query = state["messages"][-1].content.lower()

    if any(word in query for word in [
        "previous issue", "last issue", "previous support",
        "what was my previous", "history"
    ]):
        state["issue_type"] = "memory"
        return state

    elif any(word in query for word in [
        "price", "pricing", "plan", "plans",
        "subscription", "product", "software"
    ]):
        state["issue_type"] = "sales"

    elif any(word in query for word in [
        "error", "bug", "login", "install",
        "crash", "configuration", "upload"
    ]):
        state["issue_type"] = "technical"

    elif any(word in query for word in [
        "bill", "billing", "invoice", "payment",
        "refund", "charge", "charged"
    ]):
        state["issue_type"] = "billing"

    elif any(word in query for word in [
        "password", "account", "profile",
        "activate", "deactivate", "reset"
    ]):
        state["issue_type"] = "account"

    else:
        state["issue_type"] = "technical"

    print(f"\n[ROUTED TO] {state['issue_type'].upper()}")

    return state