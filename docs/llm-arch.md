# LLM Architecture

This page summarizes the H&H AI Assistant architecture and agents.

---

## Overview
The H&H AI Assistant is modular, using Streamlit for UI, Pydantic-based agents for orchestration, Supabase for data and auth, ChromaDB for embeddings, and Ollama for local LLM hosting. Langfuse is used for observability.

---

## Agents
- Master Agent: routes queries.
- General RAG Agent: document retrieval and answer generation.
- Press20 Data Agent: converts natural language to SQL and queries press20_data.
- Calculator Agent: evaluates simple math.
- Websearch Agent: performs external web searches when prefixed with `websearch.`

---

## Troubleshooting and Checklist
- Ensure network connectivity (H&H Secure/Quality or wired).
- Restart services: `python start_services.py`.
- Check Docker containers and GPU usage.

<!-- Migrated and merged from old_docs/HHDocs/docs/llm-arch.md and llm-old.md -->
