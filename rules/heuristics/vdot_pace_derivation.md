---
id: vdot_pace_derivation
tier: heuristic
statement: "When the athlete has a recent race time, derive VDOT and prescribe paces from the corresponding VDOT table; cite VDOT in the prescription."
evidence: "Daniels' Running Formula — VDOT methodology, Tables 5.1–5.2."
sources:
  - literature/daniels_running_formula.md
applies_to:
  population: [recreational, mid_level, elite]
computed_metric: "VDOT inferred from most recent race result in harness/CURRENT_STATE.md or harness/LOG.md"
status_check: "If a race result <12 weeks old is present, VDOT-derived paces should be used. If prescribed paces are inconsistent with VDOT (>10s/mi off), the rule fires."
---

# VDOT-based pace prescription

## Why
VDOT is the most reliable single-number summary of current running fitness for prescription purposes. It maps recent race performance to training paces (E, M, T, I, R) that have a coherent physiological relationship to each other.

## What the coach does
- Identify the athlete's most recent race or all-out time trial within 12 weeks.
- Derive VDOT from the time. Use the standard Daniels VDOT table.
- Prescribe:
  - **E (easy):** typically VDOT minus ~12–15 (a slower comfort pace).
  - **M (marathon):** as listed in the table.
  - **T (threshold / tempo):** as listed.
  - **I (intervals, ~5K pace):** as listed.
  - **R (repetitions, ~mile pace):** as listed.
- Always show the athlete the VDOT and the table values. Don't just hand them paces.

## When override is reasonable
- Athlete's lab/field test data (lactate, FTP analog, threshold pace) is available — prefer that over a derived VDOT.
- VDOT-derived easy pace feels too fast: trust the athlete's HR data and pull the pace back.
- Elevation, heat, terrain — adjust paces by feel/HR; cite the adjustment.

## Related rules
- `easy_day_hr_ceiling` (heuristics) — operational sanity check on derived easy pace
