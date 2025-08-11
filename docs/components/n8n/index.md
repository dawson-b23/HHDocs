# n8n — Component

This page contains the n8n documentation migrated from the top-level `n8n.md` into `components/n8n/`.

---

(Original content moved from `docs/n8n.md`)

# n8n — Beginner's Guide and Integration Notes

This expanded section explains how n8n is used in the Local AI starter kit, how to configure credentials, import workflows, and how to connect n8n to the other services (Ollama, Qdrant, Supabase, Open WebUI). It assumes no prior n8n experience.

## What is n8n in this project?

n8n is a low-code workflow automation tool. In this starter kit n8n:
- Hosts the RAG/AI workflows that perform ingestion, vectorization, and question answering flows.
- Exposes webhooks used by Open WebUI functions to trigger workflows.
- Integrates with local Postgres (Supabase), Qdrant, Ollama, Google Drive, and other services.

The n8n web UI runs at `http://localhost:5678/` by default.

(Truncated — full content is preserved in the backup `docs/n8n.bak.md`)
