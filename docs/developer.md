# Developer Notes

This page contains notes for developers onboarding to the project and direct links to key files.

## Repo layout
- `local-ai-copy/`: core application and services (Streamlit, agents, ingestion, Docker configs)
- `pydantic-model/` (if present): agent definitions and examples
- `docs/`: user-facing documentation served by Docsify

## Key files and where to look
- `local-ai-copy/start_services.py`: orchestrator script to start the full stack (Supabase + local AI services).
- `local-ai-copy/docker-compose.yml`: main compose file — inspect service names and profiles (`cpu`, `gpu-nvidia`, `gpu-amd`).
- `local-ai-copy/.env.example`: required environment variables — copy to `.env` and fill secrets.
- `local-ai-copy/Caddyfile`: example Caddy configuration for TLS and reverse proxy.
- `local-ai-copy/n8n_pipe.py`: function code to register in Open WebUI (used to connect n8n to the model UI).
- `local-ai-copy/Local_RAG_AI_Agent_n8n_Workflow.json`: n8n workflow JSON to import into n8n.
- `local-ai-copy/supabase/docker/docker-compose.yml`: local supabase configuration and initialization SQL files.
- `scripts/check_services.sh`: simple health check script (curl endpoints + `docker ps`).

## Running locally
- Copy environment: `cp local-ai-copy/.env.example local-ai-copy/.env` and fill required values. See the `.env.example` for required keys and recommended defaults.

- Start services using the orchestrator script. The project supports two environment modes (`private` and `public`) and multiple profiles for GPU support. Examples:
  - CPU (default): `python local-ai-copy/start_services.py --environment private`
  - Nvidia GPU: `python local-ai-copy/start_services.py --environment private` (the script will use the GPU-aware compose overrides if configured in your `docker-compose` and env)
  - Public deployment (locks down ports): `python local-ai-copy/start_services.py --environment public`

- The `start_services.py` script performs these steps:
  - Copies the root `.env` into `supabase/docker/.env` so Supabase picks up the same variables.
  - Stops any existing `localai` compose project (runs `docker compose -p localai -f docker-compose.yml down`).
  - Brings up Supabase first with `supabase/docker/docker-compose.yml` (plus a public override file when `--environment public` is used).
  - Waits briefly for Supabase, then brings up the local AI stack via `docker-compose.yml` (and applies `docker-compose.override.private.yml` or `docker-compose.override.public.yml` depending on the environment).

- Check containers and logs:
  - `docker compose -p localai ps`
  - `docker compose -p localai logs -f <service>`
  - `docker logs <container>` (for individual containers)

## Development tips
- Debug locations: check `local-ai-copy/logs`, `supabase/docker/volumes/*/logs`, and `neo4j` data/log folders for persistent state.
- Import workflow: open n8n at `http://localhost:5678` and import `local-ai-copy/Local_RAG_AI_Agent_n8n_Workflow.json` for the example RAG workflow.
- Open WebUI integration: add `local-ai-copy/n8n_pipe.py` as a Function in Open WebUI (Workspace → Functions → Add Function) and set its `n8n_url` to your workflow webhook URL.

<!-- Added links to key files in local-ai-copy -->