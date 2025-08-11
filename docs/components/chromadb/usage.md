# ChromaDB — Usage and Migration

Overview
- Chroma stores embeddings and supports fast nearest-neighbor searches. It offers multiple persistence options and an optional REST server.

Basic example (Python)

```
import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./chroma_db"))
collection = client.create_collection("documents")
collection.add(ids=["doc1"], metadatas=[{"title":"Doc 1"}], documents=["text content"], embeddings=[[0.1, 0.2, ...]])
results = collection.query(query_embeddings=[[0.1, 0.2, ...]], n_results=3)
```

Migration notes from Qdrant
- Export vectors from Qdrant and import into Chroma.
- For small datasets, re-ingest the original documents and compute embeddings directly into Chroma.

Integration
- Update RAG pipelines to use Chroma client endpoints or in-process client depending on deployment.

Troubleshooting
- If queries return empty results, ensure the same embedding model and dimensionality are used.
- For persistent mode, check file permissions on `persist_directory`.
