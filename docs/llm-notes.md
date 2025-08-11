# LLM Notes — Modes, Scripts, and Usage

This page summarizes the LLM-related materials in the `Work` folder and gives step-by-step instructions for running the example/testing scripts. It's written for someone with no prior experience in LLM pipelines.

---

## What the LLM assets contain

Under `Work/documents/llm/` there are several sub-folders and files:

- `additions/`: Notes and short defect lists used to seed models.
- `defects/`: Detailed cause and fix lists (`defect_causes.md`, `defect_fixes.md`).
- `docling_testing/` and `feedback/`: Example scripts and testing outputs. These include Python scripts (`main.py`) and `pyproject.toml` for dependency management.
- `from_ubuntu/files/`: Raw CSVs and processed CSVs used for experiments plus example modes (`general-mode.md`, `press20-mode.md`, `websearch-mode.md`).
- `what-can-you-do.md`: High-level description of LLM modes (General, Websearch, Press20 Data).

---

## LLM modes (from `what-can-you-do.md`)

1. General
   - Uses RAG over stored documents to answer open questions and summarize documents.
2. Websearch
   - Performs live web searches (via a configured tool) and synthesizes findings into answers.
3. Press 20 Data
   - Converts natural language to SQL queries against the `press20_data` table (useful for querying machine telemetry and shot records).

---

## How to run the example/testing scripts

Many example scripts use Python and standard tooling. Use a virtual environment and install dependencies via `pyproject.toml` or `requirements.txt` if provided.

Example (general):

1. Create a virtual environment:
   - `python -m venv .venv`
   - `source .venv/bin/activate`
2. Install dependencies (if `pyproject.toml` exists):
   - `pip install poetry` (optional) then `poetry install`, or install direct with `pip install -r requirements.txt` if a requirements file is present.
3. Run the example script:
   - `python main.py` (inspect the script to understand arguments)

Notes:
- The scripts in `docling_testing/` and `feedback/` may expect local files in a certain path — inspect the script headers for file references and update paths before running.
- If scripts use a local model or external API, ensure the local AI stack is running or update config to point at an external LLM.

---

## How these materials map to the pydantic models step

Before building Pydantic AI models, the important steps are:
1. Data discovery & normalization — use `data_descriptions.md` to standardize units and scales.
2. Create canonical defect labels and mapping — use `defect_causes.md` and `defect_fixes.md` to create label sets.
3. Build ingestion pipelines — transform CSVs into cleaned tables and vectorize documents for RAG.
4. Write Pydantic schemas representing:
   - Shot telemetry (fields, types, scales)
   - Defect reports (label, severity, timestamp, images)
   - Process sheets and maintenance logs

---

## Recommended next steps for a new engineer

- Run the data preprocessing script to convert raw CSVs to normalized Parquet/CSV using the scales documented in `data_descriptions.md`.
- Seed a small vector store (Qdrant/Chroma) with a handful of documents (defect definitions, process sheets) and test retrieval.
- Import the example n8n workflow and connect it to a toy dataset to see the end-to-end path: ingestion → vector store → RAG → LLM.

---

If you'd like, I can produce starter Pydantic schemas and a sample ingestion script (Python) that reads the Press 20 CSVs, applies scaling, and outputs cleaned Parquet files ready for ingestion into a vector store.