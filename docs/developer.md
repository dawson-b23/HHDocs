# Developer Notes

This page contains notes for developers onboarding to the project.

## Repo layout
- `local-ai-copy/`: core application and services (Streamlit, agents, ingestion, Docker configs)
- `pydantic-model/`: agent definitions and examples
- `docs/`: user-facing documentation served by Docsify

## Running locally
- Ensure you are on H&H network or have access to services.
- Start services: `python start_services.py` (wrapper to start containers and processes).
- Check containers: `docker ps` and logs in `local-ai-copy/*/logs`.

## Useful files
- `local-ai-copy/app.py`: main app entry
- `pydantic-model/ingest.py`: ingestion utilities

<!-- New supporting page created by assistant -->