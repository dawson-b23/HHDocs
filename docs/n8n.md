# n8n

Automation workflows for the H&H Local AI Project using n8n.

## Components
- General overview
- Usage patterns
- Workflows (backups, ingestion triggers)

## Common Workflows
- Trigger ingestion pipeline when new images arrive
- Backup workflows for workflows and credentials

---

# n8n — Beginner's Guide and Integration Notes

This expanded section explains how n8n is used in the Local AI starter kit, how to configure credentials, import workflows, and how to connect n8n to the other services (Ollama, Qdrant, Supabase, Open WebUI). It assumes no prior n8n experience.

## What is n8n in this project?

n8n is a low-code workflow automation tool. In this starter kit n8n:
- Hosts the RAG/AI workflows that perform ingestion, vectorization, and question answering flows.
- Exposes webhooks used by Open WebUI functions to trigger workflows.
- Integrates with local Postgres (Supabase), Qdrant, Ollama, Google Drive, and other services.

The n8n web UI runs at `http://localhost:5678/` by default.

---

## Initial setup (step-by-step)

1. Start the stack: `python local-ai-copy/start_services.py --environment private`.
2. Open the n8n UI at `http://localhost:5678/`.
3. Create a local account when prompted — this is stored in the local n8n database.

---

## Importing the example workflow

1. In n8n, go to Workflows → Import and import `local-ai-copy/Local_RAG_AI_Agent_n8n_Workflow.json`.
2. Open the workflow and review the nodes to understand how documents flow from ingestion to vector store and then to an LLM.
3. Toggle the workflow to active and copy the "Production" webhook URL — you'll use this when configuring Open WebUI function.

---

## Creating Credentials in n8n (fields and examples)

Create the following credentials so the workflow can access services. For each, after creating, click "Test" in n8n nodes to verify connectivity.

- Ollama (HTTP request credential)
  - Field: `Name` (free text)
  - Base URL: `http://ollama:11434`
  - Example (Mac host Ollama): `http://host.docker.internal:11434`

- Postgres (Database credential)
  - Host: `db` (docker service name)
  - Port: `5432`
  - Database: `postgres`
  - User: `postgres`
  - Password: value from `local-ai-copy/.env` (`POSTGRES_PASSWORD`)
  - SSL: Disable for local Docker networks

- Qdrant
  - URL: `http://qdrant:6333`
  - API key: any value locally; put it in the API Key field if the node requires one

- Google Drive (optional)
  - Follow n8n's OAuth setup: when registering credentials in Google Cloud, use a non-local redirect URI per n8n docs or rely on the local file trigger alternative.

- Additional: create HTTP Request credentials for any external webhook endpoints you need to call (e.g., maintenance ticketing systems).

---

## Node types commonly used in RAG workflows

- Webhook: receives external requests (Open WebUI/function calls) and triggers the workflow.
- HTTP Request: calls Ollama or other services when performing generation.
- Postgres: reads/writes to Supabase Postgres for metadata and vector indexes.
- Qdrant node (custom or HTTP Request): upserts and queries vectors.
- Function nodes: small JavaScript transforms used to map outputs between nodes.
- SplitInBatches + Wait: used to rate-limit vector upserts or long-running tasks.

---

## Example: test the Ollama node manually

1. Create an HTTP Request node and set method to POST.
2. URL: `http://ollama:11434/completions` with a body appropriate for the Ollama API (refer to Ollama docs).
3. Execute node to validate model responds.

---

## Debugging and logs (expanded)

- View n8n container logs:
  - `docker compose -p localai logs -f n8n`
- If a node fails during execution:
  - Open the workflow, click the failing node, and inspect the execution log panel for error details.
  - Use "Execute Workflow" on a test input to step through nodes.
- Common failures:
  - Credential errors: verify the credential under Credentials → Test.
  - Network errors: confirm service names resolve (`db`, `qdrant`, `ollama`). Use `docker compose -p localai exec n8n ping db` to test DNS inside the n8n container.

---

## Backup and restore workflows

- Export workflows and credentials regularly (Workflows → Export and Credentials → Export).
- To create an automated workflow backup, you can create an n8n workflow that periodically exports workflows via API and writes to Supabase storage or a mounted volume.

---

## Tips for non-experts

- Read workflows top-to-bottom: webhooks → transforms → vectorization → LLM call.
- Use the "Execute Workflow" and "Test" features in n8n to step through nodes during setup.
- Keep credentials secure and never commit `.env`.


## Open WebUI function integration

1. In Open WebUI (http://localhost:3000), go to Workspace → Functions → Add Function.
2. Paste code from `local-ai-copy/n8n_pipe.py`.
3. In the function settings, set `n8n_url` to the workflow webhook URL copied from n8n (Production webhook).
4. Toggle the function on — it appears in the model dropdown and can trigger the n8n workflow by calling the webhook.

---

## Shared files and local file triggers

- The starter kit mounts a host folder into the `n8n` container at `/data/shared`. Use this path in file nodes.
- On the host, place files in the configured shared folder (see `docker-compose.yml` volumes) to trigger workflows that use a Local File Trigger node.

---

## Debugging and logs

- View n8n logs inside Docker: `docker compose -p localai logs -f n8n`.
- If credentials cannot connect, verify the service host (`db`, `qdrant`, `ollama`) and the `.env` values used by Supabase and other services.

---

## Tips for non-experts

- Read workflows top-to-bottom: webhooks → transforms → vectorization → LLM call.
- Use the "Execute Workflow" and "Test" features in n8n to step through nodes during setup.
- Keep credentials secure and never commit `.env`.
