# Ingestion

Documentation for data and document ingestion pipelines.

---

## Overview
Ingestion collects telemetry and documents from edge devices and pushes normalized records to Supabase and embeddings to Chroma.

---

## Steps
1. Edge capture (Raspberry Pi) saves CSV/JSON and image files.
2. Secure transfer to workstation (rsync or S3-like endpoint).
3. Normalization script (`ingest.py`) cleans data and generates metadata.
4. Insert into Supabase using service API keys.
5. Generate embeddings and upsert into Chroma vector store.

---

## Tips
- Run ingestion in a virtualenv matching `pydantic-model/requirements.txt`.
- Monitor logs in `local-ai-copy/neo4j/logs` and `local-ai-copy/logs`.

<!-- New supporting page created by assistant -->
