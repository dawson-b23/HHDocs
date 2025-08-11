# Langfuse — Observability and Tracing for LLMs

Langfuse is an optional observability platform for LLM calls. In this starter kit it is included for tracking model calls and agent observability. It requires several secrets configured in `.env`.

---

## Required environment variables

- `CLICKHOUSE_PASSWORD` — password for ClickHouse used by Langfuse.
- `MINIO_ROOT_PASSWORD` — root password for MinIO object storage used by Langfuse.
- `LANGFUSE_SALT` — salt used for Langfuse signing.
- `NEXTAUTH_SECRET`, `ENCRYPTION_KEY` — additional secrets needed by Langfuse and associated services.

## Notes

- Langfuse components should only be exposed internally unless you know how to secure ClickHouse and MinIO.
- Logs and metrics from Langfuse can help debug model latency and errors but are optional for local experimentation.

