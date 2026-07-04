from langgraph.checkpoint.sqlite import SqliteSaver
from contextlib import ExitStack

DB_PATH = "customer_support.db"

_stack = ExitStack()

memory = _stack.enter_context(
    SqliteSaver.from_conn_string(DB_PATH)
)