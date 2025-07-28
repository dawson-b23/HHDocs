# H&H AI Assistant Architecture Documentation

## Overview

The H&H AI Assistant is a modular, AI-powered web application designed for assisting with injection molding queries at H&H. It leverages Streamlit for the frontend, Pydantic for agent-based AI workflows, and integrates with backend services like Supabase (database/auth), ChromaDB (vector search), Ollama (local LLM), and Langfuse (observability). The app supports three modes:
- **General**: Retrieval-Augmented Generation (RAG) for document queries.
- **Press Data**: Natural language to SQL for querying machine data.
- **Websearch**: Web crawling and summarization for external info.

The system is Dockerized for easy deployment and persistence. Key technologies:
- **Frontend**: Streamlit (Python-based UI).
- **Backend/AI**: Pydantic Agents for tool-based reasoning, Ollama for LLM inference.
- **Databases**: Supabase (PostgreSQL for chat history, sessions, data), ChromaDB (vector embeddings for RAG).
- **Observability**: Langfuse for tracing and monitoring.
- **Other**: Async operations with asyncio/httpx, docling for converting docs -> markdown, web tools like DDGS for search and Crawl4AI for crawling.

This doc provides a comprehensive guide for understanding, troubleshooting, updating, or extending the system. Assume familiarity with Python, Docker, and basic AI concepts.

## System Components

### 1. Streamlit App (app.py)
- **Role**: Main entry point; handles UI, authentication, chat interface, and mode-based query routing.
- **Key Features**:
  - Auth: Signup/login/logout via Supabase.
  - Session Management: Loads/saves chat history/sessions from Supabase.
  - UI: Sidebar for mode select, COT toggle, session switch/rename; main chat for messages.
  - Query Processing: Routes to agents based on mode (rag_agent, press20_agent, web_search_agent).
  - Message Display: Parses responses to show agent mode, COT (Chain-of-Thought), and final output.
- **Dependencies**: Streamlit, Pydantic-AI, Supabase-py, Langfuse, httpx, OpenAI (for Ollama compat), dotenv.
- **Config**: `DEPLOY = True` enables auth; ports/env vars from .env.

### 2. Agents
Agents are defined using Pydantic-AI for tool-based, retryable LLM calls. All use Ollama as the backend LLM.

- **RAG Agent (rag_agent.py)**:
  - System Prompt: Handles document queries with tools (rag_search, list_documents, get_file_contents, query_document_rows).
  - Tools:
    - rag_search: Queries ChromaDB for similar docs.
    - list_documents: Fetches metadata from Supabase.
    - get_file_contents: Retrieves doc text from ChromaDB.
    - query_document_rows: Runs SQL on Supabase for tabular data.
  - Output Format: "Thinking: [COT]\nResponse: [Answer]".

- **SQL Agent (sql_agent.py)**:
  - System Prompt: Converts NL to SQL for `press20_data` table (schema hardcoded).
  - No tools; direct LLM call.
  - Examples in prompt for queries like counts, averages.

- **Press20 Agent (press20_agent.py)**:
  - Wrapper: Calls sql_agent to generate SQL, executes via Supabase RPC (`query_press20_data`), formats results.

- **Web Search Agent (web_search_agent.py)**:
  - System Prompt: Handles web queries with 'web_search' tool.
  - Tool: web_search – Uses DDGS for search, Crawl4AI for crawling/filtering/summarizing (Ollama for LLM filtering).
  - Config: Browser (Chromium, headless), LLM for content filtering/aggregation.

### 3. Utilities and Helpers
- **utils.py**: ChromaDB ops (client, collections, add/query/format results). Uses SentenceTransformer for embeddings.
- **database.py**: Supabase interactions (query rows, save/get chat history/sessions, create/update sessions). Async wrappers.
- **models.py**: Pydantic models for data (DocumentMetadata, Press20Data, etc.).

### 4. Backend Services
- **Supabase**: PostgreSQL DB for auth, chat_history, chat_sessions, document_metadata, press20_data. RPCs: query_document_rows, query_press20_data.
- **ChromaDB**: Vector DB for doc embeddings/search. Collection: "documents". Host: localhost:9999 (or env).
- **Ollama**: Local LLM server (models like qwen3:14b). URL: http://localhost:11434.
- **Langfuse**: Tracing/observability. Hosts at 10.0.0.21:3000; OTLP for traces.
- **Other Libs**: Crawl4AI/DDGS for web, more-itertools for batching.

## Data Flow

1. **User Query**:
   - Input in Streamlit chat → Saved to session state and Supabase.
   - Routed by mode:
     - General: rag_agent.run(query) → Tools → LLM (Ollama) → Response.
     - Press Data: press20_run(query) → sql_agent → SQL exec on Supabase → Formatted data.
     - Websearch: web_search_agent.run(query) → Tool (search/crawl) → Summary.

2. **Response Handling**:
   - Parse for "Thinking:" and "Response:".
   - Display: Agent mode, COT (if toggled), final response.
   - Save to Supabase.

3. **Auth/Session**:
   - Supabase auth → Session ID (UUID) → Load history.

4. **RAG Flow**:
   - Query → ChromaDB search → Context → LLM generate.

5. **Observability**:
   - @observe() decorators → Langfuse traces (inputs/outputs, session/user ID).

## Dependencies and Setup

- **Python Libs** (from code; generate requirements.txt with pip freeze):
  - streamlit, pydantic-ai, supabase-py, python-dotenv, langfuse, openai, httpx, chromadb, sentence-transformers, more-itertools, uuid, asyncio, logging, ddgs, crawl4ai, biopython (etc., for tools if needed).
- **Env Vars** (.env):
  - SUPABASE_URL/KEY, OLLAMA_URL, FASTAPI_URL (if used), LLM_MODEL, LANGFUSE_* keys/host, OTEL_* endpoints.
  - In Docker: Use service names (e.g., http://supabase:8000).

- **Docker Compose**:
  - Services: app (Streamlit), supabase, chromadb, ollama, langfuse (add if not present).
  - Dockerfile: Python base, install reqs, copy code, run streamlit.
  - Volumes: For dev code sync; persistence for DBs.
  - Commands: docker compose build/up -d.

## Deployment and Operations

- **Local Dev**: pip install -r requirements.txt; streamlit run app.py.
- **Docker**: Build/run compose; access http://localhost:8501.
- **Scaling**: Ollama on GPU; increase agent retries; healthchecks in compose.
- **Data Ingestion**: Not detailed; assume docs loaded to ChromaDB/Supabase externally.
- **Updates**: Edit code → docker compose build → up -d.

## Troubleshooting

- **Auth Errors**: Check Supabase logs; verify keys/URL.
- **Query Failures**:
  - LLM: Ollama down? Check model loaded.
  - ChromaDB: No collection? Ensure data ingested.
  - Supabase RPC: SQL syntax; check schema.
- **UI Issues**: Streamlit session state; clear browser cache.
- **Performance**: Slow Ollama → Smaller model or GPU.
- **Logs**: docker compose logs -f [service]; Langfuse dashboard for traces.
- **Errors**: "No response" → Check agent outputs; timeouts → Increase httpx timeout.

## Development and Extensions

- **Adding Modes/Agents**: Create new agent.py; route in app.py.
- **Tools**: Add to agents with @agent.tool; update prompts.
- **UI Changes**: Edit app.py (e.g., add components).
- **Security**: Env vars secure; auth required; no sensitive data in prompts.
- **Testing**: Unit tests for agents; manual queries.
- **Monitoring**: Langfuse for usage; add Prometheus if needed.
- **Future**: Integrate more tools; fine-tune LLM; add image/PDF handling.

For questions, review code comments or contact original dev. This doc is as of July 28, 2025—update as system evolves.
