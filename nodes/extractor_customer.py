from utils.llm import llm
import json

def extractor_customer(state):
    last_msg = state["messages"][-1].content.lower()

    if "my name is" in last_msg:
        try:
            name = last_msg.split("my name is")[1].strip().split()[0]
            state["customer_name"] = name.title()
        except:
            pass

    prompt = f"""
Extract customer information.

Message:
{last_msg}

Rules:
- If information is missing return null.
- Never return "unknown".
- Return only JSON.

Format:
{{
    "customer_name": null,
    "customer_id": null
}}
"""

    result = llm.invoke(prompt)
    raw = result.content.strip().replace("```json", "").replace("```", "").strip()

    try:
        extracted = json.loads(raw)

        if extracted.get("customer_name") and not state.get("customer_name"):
            state["customer_name"] = extracted["customer_name"]

        if extracted.get("customer_id") and not state.get("customer_id"):
            state["customer_id"] = extracted["customer_id"]

    except json.JSONDecodeError:
        pass

    return state