---
id: acute_injury_speedwork_block
tier: hard_stop
statement: "No speedwork (intervals, tempo, threshold, strides, hill reps) while any acute musculoskeletal injury is active."
evidence: "General clinical practice; load-management consensus in running medicine."
sources: []
applies_to:
  population: [all]
  conditions: [active_acute_injury]
computed_metric: "Active injury reported in last 14 days in harness/CONSTRAINTS.md without resolution noted."
status_check: "If CONSTRAINTS.md or recent chat reports an injury that is acute (within 14 days) and unresolved, this rule fires for any speedwork prescription."
---

# Acute injury — no speedwork

Speedwork generates the highest tissue loads in running. Acute injuries need lower loads, not more.

## When this fires
Any acute musculoskeletal injury reported within the last 14 days that has not been noted as resolved or cleared. Examples:
- Calf strain
- Hamstring tweak
- Knee pain altering gait
- Hip flexor strain
- Plantar fasciitis acute flare
- (Achilles is covered by its own dedicated rule, `acute_achilles_no_speedwork`.)

This rule does **not** fire for ordinary post-workout soreness from a hard session within the expected response (24–72h).

## What the coach does
1. Remove speedwork from upcoming sessions until the injury is reported as resolved.
2. Easy running is permitted only if it does not change gait or symptom severity.
3. Cross-training (bike, pool run, elliptical) is encouraged for aerobic maintenance.
4. Recommend PT consult if symptoms persist >7 days, worsen, or recur.

## Override
This rule does **not** allow speedwork override during the acute window. The athlete may keep doing easy mileage at their discretion if gait is unchanged.

## Related rules
- `acute_achilles_no_speedwork` (rules/hard_stops/) — Achilles-specific rule
- `return_to_run_post_stress_fracture` (rules/hard_stops/) — bone stress injury rule
