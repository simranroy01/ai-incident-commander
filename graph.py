from typing import TypedDict
from langgraph.graph import StateGraph
from agents.evidence_agent import get_evidence_agent
from agents.sql_agent import get_sql_agent
from agents.memory_agent import store_memory

class AgentState(TypedDict):
    query: str
    response: str
    agent: str
    trace: list


rag_agent = get_evidence_agent()
sql_agent = get_sql_agent()

def supervisor(state: AgentState):
    query = state["query"].lower()
    trace = []

    if any(word in query for word in ["how many", "count", "list", "severity", "longest"]):
        trace.append("Supervisor classified query as metrics-related")
        trace.append("Routed to SQL Agent")
        trace.append("Executed SQL on incidents table")

        result = sql_agent.invoke(state["query"])
        response = result["output"]
        agent_used = "SQL Agent"
    else:
        trace.append("Supervisor classified query as evidence-related")
        trace.append("Routed to RAG Evidence Agent")
        trace.append("Retrieved incident documents from vector store")

        result = rag_agent.invoke(state["query"])
        response = result["result"]
        agent_used = "RAG Agent"

    store_memory(state["query"], response)

    return {
        "response": response,
        "agent": agent_used,
        "trace": trace
    }



graph = StateGraph(AgentState)
graph.add_node("supervisor", supervisor)
graph.set_entry_point("supervisor")
graph.set_finish_point("supervisor")

app = graph.compile()
