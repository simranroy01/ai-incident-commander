from typing import TypedDict
from langgraph.graph import StateGraph
from agents.evidence_agent import get_evidence_agent
from agents.sql_agent import get_sql_agent
from agents.memory_agent import store_memory

class AgentState(TypedDict):
    query: str
    response: str

rag_agent = get_evidence_agent()
sql_agent = get_sql_agent()

def supervisor(state: AgentState):
    query = state["query"].lower()

    if any(word in query for word in ["how many", "count", "list", "longest", "severity"]):
        result = sql_agent.invoke(state["query"])
        response = result["output"]
    else:
        result = rag_agent.invoke(state["query"])
        response = result["result"]

    store_memory(state["query"], response)
    return {"response": response}

graph = StateGraph(AgentState)
graph.add_node("supervisor", supervisor)
graph.set_entry_point("supervisor")
graph.set_finish_point("supervisor")

app = graph.compile()
