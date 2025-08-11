# Systems Overview — High-Level Architecture and Components

This page gives a single-page, high-level view of all important systems in the H&H Molds local AI environment. Use it as a quick map: each component has a short description and a link to a dedicated page with in-depth documentation.

---

## How to use this page
- Read the component list to understand the role of each system.
- Follow links for detailed setup, troubleshooting, and operational commands.
- The "Starting Up 0–100" guide shows a step-by-step path to get from an empty server to a working system.

---

## Core orchestration
- Docker Compose project `localai`: central orchestration for all services. See `docs/starting-up-0-100.md` for start/stop commands and run profiles.

---

## Components

- **Supabase (Postgres, Auth, Storage, Functions)** — primary database and auth provider. Used for storing telemetry metadata, user accounts, and serverless functions. See: `docs/supabase.md`.

- **n8n (Low-code workflows)** — orchestrates ingestion, RAG workflows, and automations. Exposes webhooks consumed by Open WebUI functions. See: `docs/n8n.md`.

- **Open WebUI (Chat UI + Functions)** — browser interface to interact with local LLMs and call n8n via functions (e.g., `n8n_pipe.py`). See: `docs/open-webui.md`.

- **Ollama (Local model runtime)** — runs LLM models locally and provides an HTTP completions API for inference. See: `docs/ollama.md`.

- **Qdrant (Vector store)** — high-performance nearest-neighbor vector DB for embedding storage and retrieval. See: `docs/qdrant.md`.

- **Neo4j (Knowledge graph)** — optional graph database for relationship-aware retrieval (GraphRAG patterns). See: `docs/neo4j.md`.

- **Caddy (TLS reverse proxy)** — manages HTTPS, hostnames, and reverse-proxying to frontend services. See: `docs/caddy.md`.

- **SearXNG (Meta-search)** — optional privacy-respecting web search engine used by Websearch LLM mode. See: `docs/searxng.md`.

- **Langfuse / Observability stack** — optional telemetry for LLM call traces and observability (ClickHouse, MinIO). See: `docs/langfuse.md`.

---

## Data & ingestion
- **OPC UA ingestion** — scripts and parsers that extract PLC telemetry into CSVs (Work/projects/opcua_for_presses). See: `docs/opcua_for_presses.md`.
- **Fault collection app** — on-machine collector that records shot windows and operator notes. See: `docs/fault_collection_app.md`.
- **Data display / reporting** — plotting and control-chart generation scripts used for analysis and QA reports. See: `docs/data_display.md`.
- **Data descriptions & schemas** — canonical field descriptions and scaling guidance for Press20 telemetry. See: `docs/data-descriptions.md` and `schemas/press20_schema.py`.

---

## Development & testing
- **Local dev commands**: Use `python local-ai-copy/start_services.py --environment private` to start the full stack locally. See: `docs/developer.md`.
- **Ingestion sample**: `scripts/ingest_press20.py` shows a minimal pipeline to normalize CSVs and write Parquet. See: `docs/ingestion-sample.md`.

---

## Operator & troubleshooting resources
- **Defect reference**: consolidated causes and fixes for common molding defects. See: `docs/defects.md`.
- **Troubleshooting**: common errors, logs locations, and quick fixes for Supabase, SearXNG, GPU issues, and more. See: `docs/troubleshooting.md`.
- **Quick-start checklist**: condensed steps for fast provisioning and first-run validation. See: `docs/starting-up-0-100.md` (top) and `docs/work-index.md` for Work artifacts.

---

## Where to go next
- If you are setting up a server: follow `docs/starting-up-0-100.md`.
- If you are debugging data ingestion: read `docs/opcua_for_presses.md` and `docs/data-descriptions.md`.
- If you are developing models or RAG flows: use `docs/n8n.md`, `docs/llm-notes.md`, and `docs/qdrant.md`.

---

If you'd like, I can export this page as a printable architecture diagram (SVG/PDF) and add an annotated network diagram showing ports and internal service hostnames. Would you like that added?