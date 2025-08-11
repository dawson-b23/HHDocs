# Starting Up 0–100 — Complete Setup and Run Guide

This guide walks a newcomer from an empty Ubuntu server to a fully functioning local AI stack and practical usage for H&H Molds workflows, including data ingestion, running the n8n workflows, and interacting with models via Open WebUI. It is intentionally comprehensive and prescriptive — follow steps in order.

---

## High-level steps
1. Prepare an Ubuntu server (install updates, Docker, Docker Compose, and required system packages).
2. Clone the HHDocs repository and inspect `local-ai-copy/` and `Work/` resources.
3. Prepare environment variables in `local-ai-copy/.env`.
4. Start Supabase and local AI stack using `start_services.py`.
5. Configure n8n, import workflows, and connect credentials.
6. Ingest example Press20 data and seed the vector store.
7. Use Open WebUI with the `n8n_pipe` function to interact with workflows and models.

---

## 1) Ubuntu server preparation (fresh machine)

Recommended: Ubuntu 22.04 LTS. Steps below assume root or sudo privileges.

1. Update OS packages:

    sudo apt update && sudo apt upgrade -y

2. Install essential tools:

    sudo apt install -y git curl wget build-essential ca-certificates gnupg lsb-release

3. Install Docker:

    # Install Docker's official GPG key and repository
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt update
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

4. Give your user permission to run Docker (optional but convenient):

    sudo usermod -aG docker $USER

   Log out and back in for group changes to apply.

5. Install Python3 and pip:

    sudo apt install -y python3 python3-venv python3-pip

6. (Optional) Install NVIDIA Docker runtime for GPU support if using Nvidia GPUs. Follow NVIDIA and Docker docs; ensure drivers installed.

---

## 2) Clone repo and inspect

1. Clone the HHDocs repo to `/opt` or your preferred directory:

    git clone <path-to-repo> hhdocs && cd hhdocs

2. Review these folders:
- `local-ai-copy/` — self-hosted AI starter kit and orchestration scripts
- `Work/` — project artifacts, data, and scripts used during the internship

---

## 3) Prepare `.env` and secrets

1. Copy `.env.example` to `.env` in the `local-ai-copy` directory:

    cp local-ai-copy/.env.example local-ai-copy/.env

2. Edit `local-ai-copy/.env` and set required values (generate secure values with `openssl rand -hex 32`):
- N8N_ENCRYPTION_KEY
- N8N_USER_MANAGEMENT_JWT_SECRET
- POSTGRES_PASSWORD
- JWT_SECRET
- ANON_KEY, SERVICE_ROLE_KEY
- NEO4J_AUTH
- CLICKHOUSE_PASSWORD, MINIO_ROOT_PASSWORD, LANGFUSE_SALT, NEXTAUTH_SECRET, ENCRYPTION_KEY

3. (If exposing publicly) set hostnames and `LETSENCRYPT_EMAIL` for Caddy in `.env`.

Notes:
- Use strong random secrets; do not commit `.env` to source control.
- Avoid `@` in Postgres password or percent-encode it in connection strings.

---

## 4) Start the stack

1. From repository root, run the orchestrator (private environment recommended for initial setup):

    python3 local-ai-copy/start_services.py --environment private

2. What this does:
- Copies `.env` to `supabase/docker/.env`
- Brings up Supabase (`supabase/docker/docker-compose.yml`) first
- Waits and then brings up local AI services defined in `docker-compose.yml`

3. Check status:

    docker compose -p localai ps
    docker compose -p localai logs -f n8n

Allow several minutes for services (e.g., Ollama) to download models the first time.

---

## 5) Configure n8n and Open WebUI

1. Open n8n UI: http://<server-ip-or-hostname>:5678
   - Create a local account when prompted.
2. Import workflow:
   - Workflows → Import → select `local-ai-copy/Local_RAG_AI_Agent_n8n_Workflow.json`
3. Create credentials:
   - Ollama: `http://ollama:11434` (or `host.docker.internal:11434` if running Ollama on macOS host)
   - Postgres: host `db`, port `5432`, db `postgres`, user `postgres`, password from `.env`
   - Qdrant: `http://qdrant:6333` (API key optional locally)
4. Open Open WebUI (`http://<server>:3000`) → Workspace → Functions → Add Function.
   - Paste `local-ai-copy/n8n_pipe.py` and set the `n8n_url` to the Production webhook of your n8n workflow.
   - Toggle the function on.

---

## 6) Ingest example data and seed vector store

1. Use the provided ingestion script to normalize Press20 CSVs:

    python3 scripts/ingest_press20.py Work/documents/llm/from_ubuntu/files/press20_processed.csv /tmp/press20_clean.parquet

2. Load into your database or vector store:
- For Qdrant: use their Python client to create a collection and upsert vectors.
- For Supabase vector tables: follow Supabase Functions / Vector examples.

3. Validate data in n8n workflows or small test scripts.

---

## 7) Using the model (Open WebUI + n8n)

1. From Open WebUI, choose your model and the `n8n_pipe` function to trigger the RAG workflow.
2. Interact with the model: ask general questions or Press20-specific queries (the workflow will perform retrieval and call the LLM).
3. Monitor logs in both Open WebUI and n8n for webhook activity.

---

## 8) Hardening for production

1. Use `--environment public` when running `start_services.py` after configuring DNS and ensuring ports 80/443 are open.
2. Configure Caddy hostnames in `.env` and validate DNS A records.
3. Restrict access to sensitive services (Ollama, Neo4j) or place them behind authentication.
4. Regular backups: Postgres data folder and Neo4j data.

---

## Appendices

- Troubleshooting tips are available in `docs/troubleshooting.md`.
- Detailed component guides: `docs/supabase.md`, `docs/n8n.md`, `docs/neo4j.md`, `docs/open-webui.md`, `docs/ollama.md`, `docs/qdrant.md`.


Follow this guide step-by-step and ask for clarifications at any point. I can also produce a condensed one-page checklist for operators or a shell script that automates server setup (apt installs + docker installs) if you want.