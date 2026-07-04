from langgraph.graph import StateGraph, END
from graph.customer_state import CustomerState
from graph.router import agent_router
from nodes.extractor_customer import extractor_customer
from nodes.classifier import classify_query
from nodes.rag_node import rag_node
from nodes.approval import approval
from agents.sales_agent import sales_agent
from agents.technical_agent import technical_agent
from agents.billing_agent import billing_agent
from agents.account_agent import account_agent
from agents.memory_agent import memory_agent
from agents.supervisor_agent import supervisor_agent
from memory.checkpoint import memory
def build_graph():

    builder = StateGraph(CustomerState)
    builder.add_node("extract_customer", extractor_customer)
    builder.add_node("classify_query", classify_query)
    builder.add_node("rag", rag_node)

    builder.add_node("sales", sales_agent)
    builder.add_node("technical", technical_agent)
    builder.add_node("billing", billing_agent)
    builder.add_node("account", account_agent)

    builder.add_node("memory", memory_agent)

    builder.add_node("approval", approval)
    builder.add_node("supervisor", supervisor_agent)
    builder.set_entry_point("extract_customer")
    builder.add_edge(
        "extract_customer",
        "classify_query"
    )
    builder.add_conditional_edges(
        "classify_query",
        agent_router,
        {
            "sales": "rag",
            "technical": "rag",
            "billing": "rag",
            "account": "rag",
            "memory": "memory"
        }
    )
    builder.add_conditional_edges(
        "rag",
        agent_router,
        {
            "sales": "sales",
            "technical": "technical",
            "billing": "billing",
            "account": "account"
        }
    )
    builder.add_edge("sales", "approval")
    builder.add_edge("technical", "approval")
    builder.add_edge("billing", "approval")
    builder.add_edge("account", "approval")
    builder.add_edge("approval", "supervisor")
    builder.add_edge("supervisor", END)
    builder.add_edge("memory", END)
    return builder.compile(
        checkpointer=memory
    )