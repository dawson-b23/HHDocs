# Sample Ingestion — Press20 CSV to Parquet

This page explains how to use the provided ingestion script to convert raw Press20 CSV files into cleaned Parquet files suitable for ingestion into databases or vector stores.

---

## Files created
- `scripts/ingest_press20.py` — ingestion script that applies scaling and validation.
- `schemas/press20_schema.py` — simple Pydantic model used to validate rows.

## Usage
1. Install dependencies in a virtual environment:
   - `python -m venv .venv && source .venv/bin/activate`
   - `pip install pandas pydantic pyarrow`
2. Run the ingestion script:
   - `python scripts/ingest_press20.py Work/documents/llm/from_ubuntu/files/press20_processed.csv output.parquet`
3. Output: `output.parquet` — contains normalized numeric fields and only validated rows.

## Notes
- The schema is intentionally minimal; extend `schemas/press20_schema.py` with more fields as needed.
- The scaling factors are defined in `scripts/ingest_press20.py` and reflect conversions documented in `docs/data-descriptions.md`.
- When adding new fields, ensure you add scales and Pydantic types.

