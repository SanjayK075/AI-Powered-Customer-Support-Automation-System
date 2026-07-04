from typing import TypedDict, Optional, Annotated
from langgraph.graph.message import add_messages

class CustomerState(TypedDict):
    messages: Annotated[list, add_messages]

    customer_name: Optional[str]
    customer_id: Optional[str]

    issue_type: str
    department: str

    retrieved_context: str

    approval_required: bool
    approval_status: str

    response: str