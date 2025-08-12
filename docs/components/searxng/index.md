# SearXNG — Setup and First-Run Notes

SearXNG is a meta search engine included for privacy-preserving web search. It needs a secret key configured in `searxng/settings.yml` and may require permission fixes on first run.

---

## First-run secret key

- The orchestrator has a helper to create `searxng/settings.yml` from `settings-base.yml` and replace the placeholder `ultrasecretkey` with a generated random key.
- If you prefer to do this manually on Linux/macOS:
  - Linux: `sed -i "s|ultrasecretkey|$(openssl rand -hex 32)|g" searxng/settings.yml`
  - macOS: `sed -i '' "s|ultrasecretkey|$(openssl rand -hex 32)|g" searxng/settings.yml`
  - Windows (PowerShell): follow the commands in `start_services.py`'s helper.

## Permissions

- If SearXNG containers restart repeatedly, set the folder permission: `chmod 755 searxng` so uWSGI can create its ini file.

## Troubleshooting

- Check logs: `docker compose -p localai logs -f searxng`.
- If uwsgi.ini is missing, ensure the service can write to its config directory and that `settings.yml` exists.
