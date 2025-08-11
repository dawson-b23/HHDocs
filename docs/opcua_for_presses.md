# OPC UA for Presses — Project Guide

This project ingests OPC UA data from injection presses (e.g., Press 20) and converts raw PLC outputs into CSVs suitable for analysis and ingestion into ML pipelines.

---

## Purpose

- Extract machine telemetry (positions, pressures, temps, timestamps) from PLC/OPC UA servers.
- Convert datatype codes and raw numeric representations into human-readable and scaled values.
- Produce CSVs that feed the data ingestion and analysis pipelines.

---

## Key scripts and files

- `src/convert_i_values.py` — converts OPC UA numeric type codes (e.g., `i=9`) into human-readable DataType names in a CSV dump. Usage:
  - `python src/convert_i_values.py` (adjust input/output filenames in the script or modify to accept CLI args).
- `parse.py`, `multi-parse.py` — utilities in `csv_files/` for parsing raw dump formats into structured CSVs (see comments in the scripts).
- `copy_press/create_opcua_server.py` and `copy_press/copy_opcua_server.py` — example scripts to create or copy a local OPC UA server for testing.
- `f_milacron/press20.py` and `press20_walkthrough_all_required_nodes.py` — vendor-specific explorations to identify required nodes and mapping for Press 20.

---

## Typical workflow

1. Obtain a PLC/OPC UA dump (`plc_global_pv_dump.csv` or a direct OPC UA connection).
2. Run `src/convert_i_values.py` to annotate types and produce `plc_global_pv_dump_processed.csv`.
3. Use the parsing utilities under `csv_files/` to extract time series and event windows into `press20_*.csv` files.
4. Validate and map fields against `Work/documents/llm/data_descriptions.md` to apply proper scaling.
5. Feed cleaned CSVs into the ingestion pipeline (vectorization or DB load).

---

## Running and environment

- Use a Python virtualenv and install dependencies listed in `pyproject.toml` if present.
- Many scripts assume files exist locally in the project root; review and update file paths if running from a different working directory.

---

## Troubleshooting

- If `convert_i_values.py` fails due to missing columns, inspect `plc_global_pv_dump.csv` headers for differences in naming.
- When parsing, check for delimiter or encoding issues — some PLC exports use nonstandard CSV formatting.

---

## Next steps and improvements

- Add CLI arg parsing to `convert_i_values.py` (input/output path, mapping file) for robustness.
- Standardize output schema and produce Parquet files with typed columns for downstream data pipelines.
- Add unit tests for parsing scripts to guard against varied PLC export formats.

