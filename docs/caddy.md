# Caddy — TLS and Reverse Proxy Guide

Caddy is used to provide HTTPS/TLS and reverse-proxy frontends (n8n, Open WebUI, Supabase Studio) when exposing the stack publicly. This guide explains how to configure Caddy via the `Caddyfile` and `.env` host variables.

---

## Quick overview

- Caddy reads `local-ai-copy/Caddyfile` for routing rules and will automatically obtain Let's Encrypt certificates if hostnames and `LETSENCRYPT_EMAIL` are set in `.env`.
- Recommended approach: Only expose front-end services (n8n, Open WebUI, Supabase Studio) and keep backend services (Ollama, Neo4j) restricted.

---

## Configuring hostnames

1. Set hostnames in `.env` (uncomment & replace):
   - `N8N_HOSTNAME=n8n.yourdomain.com`
   - `WEBUI_HOSTNAME=openwebui.yourdomain.com`
   - `FLOWISE_HOSTNAME=flowise.yourdomain.com`
   - `SUPABASE_HOSTNAME=supabase.yourdomain.com`
   - `OLLAMA_HOSTNAME=ollama.yourdomain.com` (not recommended for public exposure)
   - `SEARXNG_HOSTNAME=searxng.yourdomain.com`
   - `NEO4J_HOSTNAME=neo4j.yourdomain.com`
   - `LETSENCRYPT_EMAIL=you@yourdomain.com`

2. Add DNS A records pointing these subdomains to your server IP.

3. Start the stack in `public` environment to apply public overrides: `python local-ai-copy/start_services.py --environment public`.

---

## Security notes

- Caddy will terminate TLS and forward traffic to internal Docker service names. Use it as the single public entry point.
- Do not expose Ollama or Neo4j unless you secure them (authentication, IP allowlists, or put them behind Caddy with additional auth).

---

## Troubleshooting

- If certificates fail to issue, check DNS A records and ensure ports 80 and 443 are reachable.
- Check Caddy logs: `docker compose -p localai logs -f caddy`.

