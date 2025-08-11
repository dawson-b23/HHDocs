# Data Display Project — Guide

This project contains scripts and datasets for generating control charts and visual reports for enclosure data (Top/Bottom/Compact). It was used to prepare visual summaries for review and send to stakeholders.

---

## Purpose

- Read processed CSVs (e.g., `Compact Top Enclosure Data.csv`) and produce control charts and statistical summaries.
- Provide visual artifacts for process monitoring and capability analysis.

---

## Key files

- `main.py` — primary script to generate charts. Inspect the script header for required dependencies and input filenames.
- `Bottom Enclosure Data Rev 1.csv`, `Compact Top Enclosure Data.csv`, etc. — source CSVs for plotting.
- `send_to_paul/` — contains generated control chart PNG files used in reports.
- `pyproject.toml` — lists Python dependencies.

---

## How to run

1. Create and activate a virtual environment:
   - `python -m venv .venv`
   - `source .venv/bin/activate`
2. Install required packages (see `pyproject.toml` or `requirements.txt`):
   - `pip install -r requirements.txt` or use `poetry install`.
3. Run the main script:
   - `python main.py`

Notes:
- Ensure CSV filenames match those expected by `main.py` or update the script accordingly.
- Charts are saved to `send_to_paul/`.

---

## Next steps

- Convert `main.py` into a modular plotting utility accepting CLI args.
- Add a small web dashboard (Streamlit) to interactively explore datasets.

