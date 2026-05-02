---
id: progression_single_run_jump
tier: strong_guideline
statement: "A single run's distance should not exceed 110% of the longest run completed in the prior 30 days."
evidence: "BJSM 2025 — single-run progression identified as a primary risk factor for running injury, dominating week-over-week volume change."
sources:
  - literature/bjsm_2025_single_run_progression.md
applies_to:
  population: [novice, recreational, mid_level]
computed_metric: "max(distance_mi) over harness/LOG.md entries in last 30 days"
status_check: "Compare each prescribed long run to the max single-run distance in the last 30 days from LOG.md. If prescribed > 1.10 * max, the rule fires."
---

# Single-run progression

This is the single most important volume-management rule in V1.

## Why
The strongest recent evidence (BJSM 2025) finds that **single-run distance jumps** — not week-over-week mileage changes — are the dominant predictor of running injury for recreational runners. The takeaway is to grow your longest run gradually and let weekly volume follow.

## What the coach does
- When prescribing a long run, check the max single-run distance from `harness/LOG.md` in the last 30 days.
- If the prescribed long run is >110% of that max: this rule fires.
- If the rule fires: dial the prescribed long run back, OR auto-justify in the reply if the deviation is small (<5 percentage points over) and explain the reasoning, AND log the deviation to `harness/RULES_VIOLATIONS.md`.

## When override is reasonable
- Athlete is returning to a previously well-established volume after a brief layoff (in this case the 30-day window is misleading; use longer history).
- Athlete is doing a planned tune-up race or time trial as a long run, with appropriate recovery the following week.
- The "longest run in last 30 days" is anomalously short due to taper/recovery — use a 60-day window if 30 days isn't representative.

## Related rules
- `progression_weekly` (strong_guidelines) — weekly volume progression
- `long_run_share_of_volume` (heuristics) — long run as % of weekly volume
