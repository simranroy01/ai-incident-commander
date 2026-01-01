# AI Incident Commander (Agentic GenAI System)

## Overview
AI Incident Commander is an agentic GenAI backend system designed to analyze historical production incidents.
Instead of a generic chatbot, the system behaves like an incident-response assistant that retrieves evidence,
queries structured metrics, and recalls historical context.

## Key Features
- Multi-agent architecture using LangGraph
- Retrieval-Augmented Generation (RAG) over incident reports
- SQL Agent for structured incident metrics
- Deterministic supervisor-based routing
- Long-term summarized memory using MongoDB
- Clean backend-first design (no vibe coding)

## Architecture
User queries are routed by a LangGraph supervisor agent to:
- Evidence Agent (RAG) for root-cause analysis
- Metrics Agent (SQL) for counts, severity, and durations
- Memory Agent (MongoDB) for historical context

## Tech Stack
- Python
- LangChain
- LangGraph
- OpenAI (LLM + Embeddings)
- ChromaDB (Vector Store)
- SQLite (Structured Metrics)
- MongoDB (Long-term Memory)

## Example Queries
- What caused payment outages in 2024?
- How many payment incidents happened in 2024?
- Have we seen similar incidents before?

## Why This Project
Incident response naturally requires:
- Evidence aggregation
- Structured + unstructured reasoning
- Historical context

This makes it a strong real-world use case for agentic AI systems.

## Future Improvements
- Replace rule-based routing with LLM-based intent classification
- Add time-series metrics (Prometheus-style)
- Production deployment with authentication
