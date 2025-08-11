# Fault Collection App — Guide

This project collects shot-level telemetry and stores raw and processed shot data for analysis and defect correlation. It includes a TUI/GUI for operators and scripts for collecting and archiving shot logs.

---

## Purpose

- Capture shot data from presses and save time-windowed shot files for later analysis.
- Provide an operator interface (TUI/GUI) for collecting contextual notes and marking defective shots.

---

## Key files

- `main.py` — main application entry point (inspect for CLI options and data directories).
- `best_working_version.py` — a stable version used in production.
- `collected_data/` — directory containing raw/unprocessed shot data files.
- `shot_data_dir/` — structured shot data outputs grouped by date.
- `install_instructions.txt` — Pi installation instructions for deploying the collector on Raspberry Pi or similar devices.

---

## Running the app

1. Create and activate a Python virtual environment.
2. Install dependencies via `pyproject.toml` or `pip install -r requirements.txt` if available.
3. Run the app: `python main.py` or `python best_working_version.py`.
4. Collected data will be written to `collected_data/` and `shot_data_dir/`.

---

## Notes for deploy on Raspberry Pi

- Use `install_instructions.txt` and the `install_instructions_pis/README` to configure the Pi.
- Ensure the Pi has sufficient disk space and network access to transfer collected logs to a central server.

---

## Next steps

- Add data validation and schema checks before saving shot data.
- Add automated uploads from the Pi to the central Supabase/Postgres instance or object storage for centralized ingestion.

