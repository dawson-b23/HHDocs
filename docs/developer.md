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
1. Copy environment: `cp local-ai-copy/.env.example local-ai-copy/.env` and fill required values.
2. Start services (profile depends on GPU):
   - `python local-ai-copy/start_services.py --profile cpu`
   - `python local-ai-copy/start_services.py --profile gpu-nvidia`
3. Check containers: `docker ps` and `docker logs <container>`.

## Development tips
- When debugging agent code, look in `local-ai-copy/logs` and n8n workflow logs.
- For quick experiments, import `Local_RAG_AI_Agent_n8n_Workflow.json` into n8n via the UI at `http://localhost:5678`.

<!-- Added links to key files in local-ai-copy -->