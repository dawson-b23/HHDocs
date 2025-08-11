# Supabase — Component

This page contains the Supabase documentation migrated from the top-level `supabase.md` into `components/supabase/`.

---

(Original content moved from `docs/supabase.md`)

# Supabase — Local Hosting Guide

This page explains how Supabase is used in the Local AI starter kit, how to configure it locally, and common maintenance tasks. The target reader has no prior Supabase experience — the instructions are step-by-step and include troubleshooting hints.

**Goals:**
- Explain what Supabase provides in this stack.
- Show how to prepare `.env` values and start Supabase.
- Describe important filesystem locations and initialization SQL.
- Provide common troubleshooting steps and recovery commands.

---

## What is Supabase in this project?

Supabase provides:
- PostgreSQL database (used by n8n and other services).
- Auth (GoTrue) for user sign-in and session handling.
- Storage for files.
- Functions (serverless) for custom backend logic.

In this starter kit Supabase is the authoritative DB and can also be used as a vector store for RAG (though Qdrant or Chroma may be preferred).

---

## Preparing the environment

1. Copy and edit the `.env` file:
   - `cp local-ai-copy/.env.example local-ai-copy/.env`
   - Edit `local-ai-copy/.env` and set the required variables under the "Supabase" section:
     - `POSTGRES_PASSWORD` — choose a long, secure password (avoid `@` if possible).
     - `JWT_SECRET` — at least 32 characters.
     - `ANON_KEY` and `SERVICE_ROLE_KEY` — JWT keys used by Supabase APIs.
     - `DASHBOARD_USERNAME` and `DASHBOARD_PASSWORD` — default Supabase studio credentials.
     - `POOLER_TENANT_ID` — integer (any value, e.g., `1000`).

2. Check optional service variables (change only if you understand implications):
   - `POOLER_DB_POOL_SIZE=5` — required for some legacy setups.
   - `STUDIO_PORT` and `SUPABASE_PUBLIC_URL` if you want a different local port or public URL.

---

## How Supabase is started

The orchestrator script copies the root `.env` into `supabase/docker/.env` so that Supabase's own docker-compose uses the same environment variables.

Sequence when starting the package:
1. `python local-ai-copy/start_services.py --environment private`
2. The script runs: `docker compose -p localai -f supabase/docker/docker-compose.yml -f docker-compose.override.public.supabase.yml up -d` (override file applied if `--environment public`).
3. Wait for Postgres to initialize; some services (analytics) run initialization SQL and may take a few minutes on first boot.

To run Supabase by itself (advanced):
- `docker compose -p localai -f local-ai-copy/supabase/docker/docker-compose.yml up -d`

---

## Important files and directories

- `local-ai-copy/supabase/docker/.env` — copied from root `.env` by the orchestrator. Contains runtime secrets for Supabase.
- `local-ai-copy/supabase/docker/docker-compose.yml` — Supabase compose definition used by the starter kit.
- `local-ai-copy/supabase/docker/volumes/db/init/` — initialization SQL scripts that populate schemas, roles, and required objects.
- `local-ai-copy/supabase/docker/volumes/db/data/` — persistent Postgres data. If corrupted or if passwords change, this folder may need to be deleted to reinitialize.

---

## Connecting from other services

- Use `POSTGRES_HOST=db` (the Docker Compose service name). From the host machine, to connect use `localhost` and the mapped port if exposed.
- Use `POSTGRES_USER=postgres`, `POSTGRES_DB=postgres`, and the `POSTGRES_PASSWORD` you set in `.env`.
- In n8n create a Postgres credential with host `db`, port `5432`, database `postgres`, user `postgres`, password `POSTGRES_PASSWORD`.

---

## Functions and security

- Functions are controlled by `FUNCTIONS_VERIFY_JWT` in `.env`. By default it is `false` for convenience in local setups.
- For production, enable JWT verification and protect function endpoints.

---

## Common problems and fixes

1. Supabase containers crash or refuse to start after password change:
   - Stop Supabase: `docker compose -p localai -f supabase/docker/docker-compose.yml down`
   - Remove DB data: `rm -rf local-ai-copy/supabase/docker/volumes/db/data`
   - Restart Supabase via the orchestrator to reinitialize with new `.env` values.

2. Supabase pooler keeps restarting:
   - Check `supavisor` configuration and `POOLER_*` variables in `.env`.
   - Inspect logs: `docker compose -p localai -f supabase/docker/docker-compose.yml logs -f supabase-pooler`

3. Supabase service cannot be contacted from other containers:
   - Ensure the `localai` compose project is running and the service name `db` resolves inside the Docker network.
   - Check container health: `docker compose -p localai ps`

---

## Maintenance and upgrades

- To pull newer Supabase images and re-run initializers:
  - `docker compose -p localai -f supabase/docker/docker-compose.yml pull`
  - `docker compose -p localai -f supabase/docker/docker-compose.yml up -d`
- When changing sensitive secrets (DB passwords), reinitialize DB volumes if you cannot migrate them.

---

## Init SQL files — purpose, exact effects, and commands

This starter kit contains several SQL scripts executed during Supabase initialization. Below is a detailed, operational reference that includes the exact effect of each script and commands you can run to inspect or reproduce the changes.

### `_supabase.sql`
- Purpose: Creates a database named `_supabase` owned by the Postgres user defined in `POSTGRES_USER`.
- Effect:
  - `CREATE DATABASE _supabase WITH OWNER :pguser;`
- Inspect or run manually:
  - Connect to Postgres as a superuser and run `\l` to list databases or run `psql -U postgres -c "\l"`.
  - To create manually: `psql -U postgres -c "CREATE DATABASE _supabase WITH OWNER postgres;"` (replace owner as needed).

### `data.sql` (empty placeholder)
- Purpose: Reserved for site-specific initial data. Currently empty.
- Guidance:
  - Add seed data here to be executed on first init. Scripts in this folder run only when the DB volume is empty.

### `jwt.sql`
- Purpose: Stores JWT configuration in the `postgres` DB settings so Supabase auth uses the configured secrets.
- Effect:
  - `ALTER DATABASE postgres SET "app.settings.jwt_secret" TO :'jwt_secret';`
  - `ALTER DATABASE postgres SET "app.settings.jwt_exp" TO :'jwt_exp';`
- Variables:
  - `JWT_SECRET`, `JWT_EXP` from `.env`.
- Inspect:
  - In psql: `SELECT name, setting FROM pg_settings WHERE name LIKE 'app.settings%';`

---

