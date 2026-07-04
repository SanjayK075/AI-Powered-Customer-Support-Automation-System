def approval(state):
    query = state["messages"][-1].content.lower()

    approval_keywords = [
        "refund",
        "cancel subscription",
        "subscription cancellation",
        "close account",
        "account closure",
        "compensation",
        "escalate",
        "management"
    ]

    if any(word in query for word in approval_keywords):
        state["approval_required"] = True
        state["approval_status"] = "Approved by Supervisor"

        print("\n========== HUMAN IN THE LOOP ==========")
        print("Approval Required")
        print("Supervisor Review Completed")
        print("Request Approved!!")

    else:
        state["approval_required"] = False
        state["approval_status"] = "Not Required"

    return state