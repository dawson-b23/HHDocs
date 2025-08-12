#!/usr/bin/env python3
"""
Simple ingestion script for Press20 CSVs.
- Reads a CSV exported from the Work folder
- Applies scaling rules (as in docs/data-descriptions.md)
- Validates rows with Pydantic models
- Outputs cleaned Parquet for downstream use

Usage:
    python scripts/ingest_press20.py input.csv output.parquet

This script is intentionally small and easy to adapt.
"""
import sys
import pandas as pd
from pathlib import Path
from schemas.press20_schema import Press20Row

SCALES = {
    'actcycletime': 0.01,
    'actclpclstime': 0.01,
    'actcoolingtime': 0.01,
    'actfill': 0.01,
    'actfilltime_0': 0.01,
    'actfilltime_1': 0.01,
    'actfilltime_2': 0.01,
    'actinjfwdstagetime_0': 0.01,
    'actinjfwdstagetime_1': 0.01,
    'actinjfwdstagetime_2': 0.01,
    'actcushionposition': 0.0003937,
    'actinjectionpos': 0.003937,
    'actinjfillspd': 0.003937,
    # pressure fields -> multiply by 1.45038 to get psi
    'inj_act_prs_0': 1.45038,
    'inj_act_prs_1': 1.45038,
    'inj_act_prs_2': 1.45038,
    'actprocofmaxinjprs': 1.45038,
    'actccprs': 1.45038,
    'backprs_value': 1.45038,
    'actsysprsservodrive_0': 1.45038,
    'actsysprsservodrive_1': 1.45038,
    # current -> multiply by 0.1
    'actcurrentservodrive_disp_1': 0.1,
    'actcurrentservodrive_disp_2': 0.1,
    'actnozzlecurrent': 0.1,
}


def apply_scales(df: pd.DataFrame) -> pd.DataFrame:
    for col, factor in SCALES.items():
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce') * factor
    return df


def validate_rows(df: pd.DataFrame) -> pd.DataFrame:
    valid_rows = []
    errors = 0
    for idx, row in df.iterrows():
        data = row.to_dict()
        try:
            validated = Press20Row(**data)
            valid_rows.append(validated.dict())
        except Exception:
            errors += 1
            # For brevity, we skip printing every error.
    print(f"Validated {len(valid_rows)} rows, {errors} invalid rows")
    return pd.DataFrame(valid_rows)


def main():
    if len(sys.argv) < 3:
        print("Usage: ingest_press20.py input.csv output.parquet")
        sys.exit(1)
    input_csv = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    df = pd.read_csv(input_csv)
    df = apply_scales(df)
    df_clean = validate_rows(df)
    df_clean.to_parquet(output_path, index=False)
    print(f"Wrote cleaned data to {output_path}")


if __name__ == '__main__':
    main()
