# Defects — Reference and Troubleshooting

This page aggregates defect definitions, common causes, and recommended fixes pulled from the `Work/documents/llm` folder. It's written so someone with no experience in injection molding can diagnose and apply corrective actions.

---

## How to use this page

- Start with the "Defect Description" to visually identify the problem.
- Refer to "Common Causes" to find probable process parameters or tooling issues.
- Apply the "Recommended Fixes" systematically — change one variable at a time and record results.

---

## Common defects (short list)
- Cold slugs
- Glass Lines
- Gate Blush
- Warp / Mismatch / FFF
- Flash

---

## Example defect entries (detailed)

### Cold Slug
- Description: Solidified material at the nozzle or entry that creates a cold region in the flow, causing incomplete fusion and surface defects.
- Common Causes:
  - Nozzle temperature too low.
  - Insufficient cold slug well.
  - Low injection pressure or small runner size.
- Recommended Fixes:
  - Increase nozzle temperature by 5°C.
  - Increase melt temperature by 5°C.
  - Increase injection pressure by 100 psi.
  - Adjust screw speed slightly to improve melt homogeneity.

### Glass Lines
- Description: Visible lines or weld areas in fiber-filled materials where fibers do not knit properly.
- Common Causes:
  - Low melt temperature or slow injection speed leading to premature cooling.
  - Poor venting or insufficient packing pressure.
- Recommended Fixes:
  - Increase melt temperature by 5°C.
  - Increase injection speed by 10%.
  - Increase pack pressure by 100 psi.

### Blush / Gate Blush
- Description: Surface haze or discoloration usually near the gate.
- Common Causes:
  - High shear at gate due to rapid injection.
  - Moisture in resin.
  - Low mold temperature.
- Recommended Fixes:
  - Decrease injection speed by 10%.
  - Increase mold and melt temperature by 5°C as needed.
  - Profile injection speed to start slower near the gate.

### Flash
- Description: Thin excess material at the parting lines or vents.
- Common Causes:
  - Excessive injection pressure, inadequate clamp force, or worn/misaligned mold.
- Recommended Fixes:
  - Decrease injection pressure by 100 psi.
  - Increase clamp force by 5 tons if adjustable.
  - Inspect and service mold alignment and wear.

---

## Full lists and detailed guidance
I extracted the comprehensive lists of causes and fixes from the following files in the `Work` folder:
- `Work/documents/llm/defects/defect_causes.md`
- `Work/documents/llm/defects/defect_fixes.md`
- `Work/documents/llm/additions/common_defects.md`

For full reference, consult these source files in the repository. If you'd like, I can also:
- Convert each cause/fix pair into a troubleshooting checklist (one-liner action items) for use on the shop floor.
- Create printable quick-reference cards for operators.

Which would you prefer next?