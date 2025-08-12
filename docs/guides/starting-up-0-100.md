# Starting Up 0→100 (Ubuntu → Running Everything)

This guide shows step-by-step instructions to set up a fresh Ubuntu machine and get the HHDocs environment and related services running. It targets someone starting from a default Ubuntu installation (22.04/24.04 LTS). Follow each section and adapt versions where needed.

---

## 1. System basics
- Update packages: `sudo apt update && sudo apt upgrade -y`
- Install common tools: `sudo apt install -y build-essential curl wget git ca-certificates gnupg lsb-release`
- Create a user if needed and set sudo: `sudo adduser <username> && sudo usermod -aG sudo <username>`

---

## 2. Install development tools
- Install Python (recommended via `pyenv`) or system Python:
  - System: `sudo apt install -y python3 python3-venv python3-pip`
  - pyenv (optional): follow `https://github.com/pyenv/pyenv` install steps, then install desired Python versions.
- Install Node.js (for docs tooling) via NodeSource or `nvm`:
  - `curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - && sudo apt-get install -y nodejs`
- Install `pipx` for isolated CLI installs: `python3 -m pip install --user pipx && python3 -m pipx ensurepath`

---

## 3. Git and repository setup
- Clone the repo: `git clone <repo-url> && cd HHDocs`
- Configure git: `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`

---

## 4. Virtual environments and dependencies
- Create and activate venv: `python3 -m venv .venv && source .venv/bin/activate`
- Install python deps if project provides `requirements.txt` or `pyproject.toml`:
  - `pip install -r requirements.txt` or `pip install -e .` depending on project.

---

## 5. Docs preview (Docsify)
- The repo uses Docsify static docs. You can preview locally via `docsify` or `npx docsify-cli`:
  - Install: `npm i -g docsify-cli` or `npx docsify-cli serve docs`
  - Start preview: `docsify serve docs` and open `http://localhost:3000`

---

## 6. Local AI tooling (LLMs, vector dbs)
- Optional components covered in this repo include Ollama, LocalAI, Open-WebUI, Qdrant, and Langfuse. Install steps vary; general guidance:
  - Qdrant: recommended via Docker Compose — create `docker-compose.yml` and run `docker compose up -d` (see `docs/qdrant.md` for details)
  - Ollama: install from official site (DEB or brew) — see `docs/ollama.md`
  - LocalAI / Open-WebUI: follow project pages in this repo (`docs/open-webui.md`, `docs/local-ai-copy.md`)
  - For Docker: `sudo apt install -y docker.io docker-compose && sudo usermod -aG docker $USER`

---

## 7. Databases and services
- Supabase: sign up or run locally via Docker. Follow `docs/supabase.md`.
- Neo4j: follow `docs/neo4j.md` for install and examples.

---

## 8. Ingestion and data pipelines
- Review `docs/ingestion.md` and `docs/ingestion-sample.md` for sample pipelines and scripts in `scripts/` and `Work/projects/*`.

---

## 9. Running example projects
- `Work/projects/flow-sensor` and `fault_collection_app` include README and entrypoints. Check those folders for run instructions.

---

## 10. Recommended detailed installs

### Qdrant (Docker Compose)
1. Create `docker-compose.yml` with:

```yaml
version: '3.8'
services:
  qdrant:
    image: qdrant/qdrant:latest
    restart: unless-stopped
    ports:
      - "6333:6333"
    volumes:
      - qdrant_storage:/qdrant/storage
volumes:
  qdrant_storage:
```

2. Start: `docker compose up -d`
3. Check status: `docker compose ps` and the HTTP API at `http://localhost:6333`

### Ollama (quick)
- Follow `docs/ollama.md` in this repo. Typically: download DEB or use their installer and start the Ollama daemon. Confirm with `ollama version`.

### LocalAI / Open-WebUI
- See `docs/open-webui.md` and `docs/local-ai-copy.md` for project specific instructions; many of these run in Docker and have their own config.

---

## 11. Troubleshooting & tips
- If permission denied for Docker, log out and back in after adding to `docker` group.
- Use `journalctl -u <service>` for systemd service logs.
- Keep Python virtualenv isolated; prefer `pipx` for CLI tools.

---

## 12. Next steps / checklist
- [ ] Clone repo and open `docs/` locally
- [ ] Set up Python venv and install deps
- [ ] Start docs preview with `docsify`
- [ ] Install Docker and run Qdrant (if using vector DB)
- [ ] Confirm local AI runtime (Ollama/LocalAI) if required

---
Notes: adapt versions (Ubuntu, Node, Python) to your environment. Request more detail for any specific component (Qdrant, Ollama, Supabase) and I'll expand that section.
