---
id: long_run_share_of_volume
tier: heuristic
statement: "The long run should be roughly 25–35% of weekly volume, never exceeding 35% for sustained periods."
evidence: "Daniels' Running Formula; Pfitzinger's Advanced Marathoning; coaching convention."
sources:
  - literature/daniels_running_formula.md
  - literature/pfitzinger_advanced_marathoning.md
applies_to:
  population: [novice, recreational, mid_level]
computed_metric: "long_run_distance / sum(week_distance) in plan/weeks/week_*.md"
status_check: "Compute long run as fraction of prescribed weekly volume. If > 0.35 for the week, the rule fires."
---

# Long run as % of weekly volume

## Why
A long run that's >35% of the week's volume tends to leave outsized residual fatigue and crowds out the rest of the training stimulus. Below 25% and the long run isn't doing its job for endurance development.

## What the coach does
- Aim for 25–30% in build phases.
- Up to 33% in late-block specific endurance work (especially marathon prep).
- Above 35%: this rule fires; the coach can deliver but must justify (athlete is in a low-volume week, athlete deliberately prioritizes long runs, etc.).

## When override is reasonable
- Recovery weeks where total volume is intentionally low — the long run can naturally be a larger fraction without being dangerous.
- Marathon-specific late-block runs (e.g., 22 mi long run on a 60 mi week is 37%; this is normal for marathoners).
- Athlete is deliberately running fewer days per week and packing the long run.

## Related rules
- `progression_single_run_jump` (strong_guidelines) — the dominant constraint, supersedes this heuristic
