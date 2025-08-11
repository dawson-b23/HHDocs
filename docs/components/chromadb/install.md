# ChromaDB — Install

Quick (concise)
- Install via pip inside a venv: `python3 -m venv .venv && source .venv/bin/activate && pip install chromadb`

Docker
- Chroma provides a Docker image; many projects run Chroma in-process or via the REST server. Example Docker Compose service:

```yaml
services:
  chroma:
    image: chromadb/chromadb:latest
    ports:
      - "8000:8000"
    volumes:
      - chroma_data:/chroma
volumes:
  chroma_data:
```

Notes
- Chroma can run in-process (embedded) or as a server. Choose embedded for single-process apps, and server mode when multiple services need access.
