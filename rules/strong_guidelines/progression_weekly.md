---
id: progression_weekly
tier: strong_guideline
statement: "Avoid weekly volume increases of more than 30% over the prior week. Prefer 5–10% as a steady-state ramp."
evidence: "JOSPT 2014 — week-over-week increases > 30% associated with elevated injury risk for specific subtypes (knee, lower-leg)."
sources:
  - literature/jospt_2014_weekly_progression.md
applies_to:
  population: [novice, recreational, mid_level]
computed_metric: "sum(distance_mi) per ISO week from harness/LOG.md"
status_check: "Compare prescribed weekly volume to last completed week's volume from LOG.md. If prescribed > 1.30 * last week, the rule fires."
---

# Weekly volume progression

## Why
The "10% rule" is widely repeated and has weak empirical support. The actual JOSPT 2014 cohort data finds that the meaningful threshold is **>30% week-over-week**, where injury risk for specific subtypes (patellofemoral pain, medial tibial stress syndrome) climbs noticeably.

We treat 5–10%/week as a comfortable steady-state ramp, NOT as a "rule." The hard line is at 30%.

## What the coach does
- Sum the athlete's last completed week from `harness/LOG.md`.
- Compare to the prescribed week's total volume.
- If prescribed > 1.30 × last week: rule fires.
- If 1.10 ≤ prescribed ≤ 1.30: acceptable but flag in justification.
- If recovery week: reductions of 20–30% are expected and welcome.

## When override is reasonable
- Returning from a planned recovery week (the prior week was deliberately cut).
- Returning from illness, travel, or unplanned downtime where the prior week was anomalous. Use a 4-week rolling average as the comparison baseline instead.
- First week back after a goal race recovery — start lower, not higher.

## Don't conflate this with the "10% rule"
The "10% rule" attributed to Joe Henderson / Runner's World is folk wisdom with thin evidence. Don't quote it as if it's gospel. If the athlete invokes it, you can validate the spirit (gradual progression) while citing the actual JOSPT/BJSM evidence as the source.

## Related rules
- `progression_single_run_jump` (strong_guidelines) — the dominant constraint
- `recovery_week_cadence` (strong_guidelines) — when to cut volume
