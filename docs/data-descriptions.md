# Data Descriptions — Press 20 and Machine Telemetry

This page documents the machine data fields used for Press 20 datasets and other telemetry collected on the shop floor. It summarizes each parameter, units, how to scale raw values, and what the field indicates. This is written for someone new to the dataset.

---

## How to read these parameters
- Many raw values are integers that require scaling (multiply/divide) to convert into human units.
- Typical conversions include multiplying by 0.01 for time values, 0.1 for currents, and 1.45038 to convert internal pressure units to psi.
- Always check the example rows in `Work/documents/llm/from_ubuntu/files/` CSVs when validating conversions.

---

## Key fields (selected)
- `shot_num`: Identifier for each shot (dimensionless)
- `cameratimestamp` / `machinetimestamp`: Timestamps for image capture and machine event (datetime)
- `bottompassfail`, `toppassfail`, `overallpassfail`: PASS/FAIL results from vision systems
- `bottomanomalylevel`, `topanomalylevel`: Numeric anomaly scores (dimensionless)

### Timing and cycle
- `actcycletime`: Cycle time in seconds. Scale: multiply raw value by 0.01 (e.g., 6924 → 69.24s)
- `actclpclstime`: Clamp close time (seconds). Scale: ×0.01
- `actcoolingtime`: Cooling time (seconds). Scale: ×0.01

### Injection / Motion
- `actcushionposition`: Cushion position (inches). Scale: ×0.0003937
- `actinjectionpos`: Injection position (inches). Scale: ×0.003937
- `actinjfillspd`: Injection fill speed (in/sec). Scale: ×0.003937
- `actinjfwdstagepos_*` and `actinjfwdstageprs_*`: Stage positions and pressures — positions scale ×0.003937, pressures scale ×1.45038 to get psi.

### Press pressures and forces
- `inj_act_prs_*`, `actprocofmaxinjprs`, `actsysprsservodrive_*`: Pressures (psi). Scale: ×1.45038
- `actccprs`: Clamp close pressure (psi). Scale: ×1.45038

### Temperatures
- `actnozzletemp`, `actzone*_temp`, `actoiltemp`, `acttempservodrive_*`: Temperature readings. Documentation indicates conversions like (value * 0.18 + 32) or scale factors; check examples for exact math. Example: some fields require dividing by 10 or multiplying by 0.1 after conversion.

### Motor and Servo
- `actcurrentservodrive_*`, `actnozzlecurrent`: Current in amps. Scale: multiply raw by 0.1
- `actmotorrpmservodrive_*`: RPM (direct)

### Process monitoring and derived metrics
- `actprocofmaxinjprspos`: Position where max injection pressure occurred (in). Scale: ×0.003937
- `backprs_value`: Back pressure (psi). Scale: ×1.45038

---

## Best practices for ingestion
- Normalize and scale values during preprocessing before inserting into a vector store or database. Store both raw and scaled values for traceability.
- Document any uncertain conversion formulas as metadata in the dataset; include example conversions in the dataset README.
- When in doubt, compare a few raw rows against known machine readings to validate scaling formulas.

---

## Files to reference
- Source CSVs and spreadsheets: `Work/documents/llm/from_ubuntu/files/`, `Work/documents/llm/process_sheet_mold1306_press_20.csv`, `Work/documents/llm/Mold 1306 - Press 20 - 05-21-2025.csv`.
- Data descriptions: `Work/documents/llm/data_descriptions.md` (this page was generated from that source).

If you want, I will add a small code snippet showing a canonical preprocessing function (in Python/pandas) that applies common scaling to these fields.