# Neo4j — Beginner's Guide and Maintenance Notes

Neo4j is a graph database included in the Local AI starter kit. This page explains: what Neo4j is used for here, where its data lives, how to configure credentials, and how to perform basic maintenance.

---

## What is Neo4j used for?

- Neo4j stores knowledge graphs that can be used for graph-based retrieval (GraphRAG), relationship traversal, and augmenting vector search with relational context.
- It complements vector stores (Qdrant, Supabase vectors) for use cases where graph relationships are important.

---

## Data and configuration locations

- Data files are persisted under `local-ai-copy/neo4j/data/` in the repository. This folder contains `databases/system/*` files including `neostore.*` and index directories.
- The Docker Compose service uses the `NEO4J_AUTH` environment variable for username/password (format `username/password`) — set this in `local-ai-copy/.env`.

---

## Basic operations

- Start/stop (compose project `localai`):
  - `docker compose -p localai up -d neo4j`
  - `docker compose -p localai stop neo4j`

- Check logs:
  - `docker compose -p localai logs -f neo4j`

- Connect to Neo4j Browser / Bolt endpoints depending on how you expose the service. By default this setup prefers internal access; configure Caddy if you need external browser access.

---

## Maintenance

- Backup: copy `local-ai-copy/neo4j/data/` to a safe location when the DB is offline.
- Reindex / repair: consult Neo4j documentation for steps to rebuild indexes before deleting `neostore` files. Do not manually delete Neo4j store files unless you intend to fully reset the database.

---

## Troubleshooting

- If Neo4j fails to start due to file corruption, consider restoring from backups or reinitializing the data folder (this will delete graph data):
  - `docker compose -p localai down neo4j`
  - Remove data folder: `rm -rf local-ai-copy/neo4j/data/*`
  - Start Neo4j again and recreate necessary indices and nodes.

---

If you'd like, I can add a short guide on common Cypher queries used in RAG pipelines and an example of how to export Neo4j data to CSV for offline analysis.
