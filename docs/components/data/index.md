# Data — Component

This page contains the data documentation migrated from the top-level `data.md` into `components/data/`.

---

(Original content moved from `docs/data.md`)

## Data

This page documents data sources, collection, processing, and storage for the H&H Local AI Project.

## Components
- Usage
- Injection Molding Press
- Aggregation on AI Workstation
- Raspberry Pi on Press
- Data schema and descriptions

## Overview
Data is collected from injection molding presses (e.g., press20) using Raspberry Pi gateways that stream telemetry and images to an AI workstation. The workstation aggregates, cleans, and inserts data into Supabase/Postgres and a vector store (Chroma) for retrieval.

## Data Collection
- Raspberry Pi: edge device on each press capturing sensor telemetry and camera images.
- Aggregation: AI Workstation runs ingestion pipelines to normalize and store data.
- Cleaning: Scripts normalize column names, remove corrupt records, and standardize timestamps.
- Storage: Time-series and tabular data in Postgres (Supabase); embeddings and documents in Chroma.

## Common Fields (press20_data)
- shot_num: integer — sequential shot number
- overallPassFail: PASS/FAIL
- ActCycleTime, ActNozzleTemp, etc. — sensor readings

## Insertion
- Ingestion scripts transform CSV/JSON to SQL and push to Supabase using service account keys.
