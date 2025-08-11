# Qdrant — Component

This page contains the Qdrant documentation migrated from the top-level `qdrant.md` into `components/qdrant/`.

---

(Original content moved from `docs/qdrant.md`)

## Qdrant — Vector Store Notes

Qdrant is an optional, high-performance vector database included in the starter kit. Use Qdrant for large-scale nearest neighbor searches when Supabase's vector support is not sufficient.

## Access and endpoints

- Inside Docker network: `http://qdrant:6333`.
- API key is optional for local setups; set to any string when configuring in n8n.

## Usage

- Use Qdrant when vector payloads grow large or when you need faster k-NN searches.
- n8n and ingestion processes can write vectors into Qdrant directly.

## Troubleshooting

- Inspect container logs: `docker compose -p localai logs -f qdrant`.
- Verify persistent volume configuration in `docker-compose.yml` if data is not being saved between restarts.
