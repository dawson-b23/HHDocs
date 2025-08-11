# ChromaDB — Migration from Qdrant (Export / Import)

This page documents concrete steps to migrate vectors from a Qdrant instance into ChromaDB, and includes a small ingestion example that computes embeddings and writes into Chroma.

Prerequisites
- Python 3.10+ and `pip`.
- Access to Qdrant HTTP API (`http://qdrant:6333`) or exported vector data.
- A ChromaDB instance (in-process or server) and the embedding model used previously.

1) Export vectors from Qdrant

If you can query all points, export them using the Qdrant HTTP API. Example using Python and `requests`:

```python
import requests
import json

QDRANT_URL = "http://localhost:6333"
COLLECTION = "documents"

resp = requests.post(f"{QDRANT_URL}/collections/{COLLECTION}/points/scroll", json={"limit": 10000})
resp.raise_for_status()
items = resp.json()
with open('qdrant_export.json', 'w') as f:
    json.dump(items, f)
print('Exported', len(items.get('result', [])))
```

Note: for large datasets you may need to paginate using `offset` or `next` tokens depending on Qdrant version.

2) Convert export to Chroma import format

Chroma requires `ids`, `documents`, `metadatas`, and `embeddings`. Example converter (assumes Qdrant payload contained `id`, `payload['text']`, and `vector`):

```python
import json

with open('qdrant_export.json') as f:
    data = json.load(f)

documents = []
ids = []
metadatas = []
embeddings = []
for p in data.get('result', []):
    ids.append(str(p['id']))
    embeddings.append(p['vector'])
    documents.append(p.get('payload', {}).get('text', ''))
    metadatas.append(p.get('payload', {}))

chroma_import = {
    'ids': ids,
    'documents': documents,
    'metadatas': metadatas,
    'embeddings': embeddings
}

with open('chroma_import.json', 'w') as f:
    json.dump(chroma_import, f)
print('Converted to chroma_import.json')
```

3) Import into Chroma (Python example)

```python
import chromadb
from chromadb.config import Settings
import json

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./chroma_db"))
collection = client.get_or_create_collection("documents")

with open('chroma_import.json') as f:
    payload = json.load(f)

collection.add(ids=payload['ids'], documents=payload['documents'], metadatas=payload['metadatas'], embeddings=payload['embeddings'])
print('Imported into Chroma')
```

4) Alternative: Re-ingest original documents

If you have the source documents, recompute embeddings using the same model and directly write into Chroma. This is often safer and ensures embedding dimensionality matches.

Example using `sentence-transformers` for embeddings:

```python
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./chroma_db"))
collection = client.get_or_create_collection("documents")

documents = ["Text A", "Text B"]
ids = ["a", "b"]
embs = model.encode(documents).tolist()
collection.add(ids=ids, documents=documents, embeddings=embs)
```

5) Verify

- Query Chroma and compare top-k results with Qdrant queries for a few sample vectors to validate migration fidelity.

6) Cleanup

- After verifying, decommission Qdrant or keep it for fallback. Keep backups of exported files.

If you want, I can add a small `scripts/chroma_migrate.py` file to the repo that wraps these steps and takes arguments for Qdrant URL, collection name, and Chroma DB path.
