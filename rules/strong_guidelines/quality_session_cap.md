---
id: quality_session_cap
tier: strong_guideline
statement: "Prescribe at most two quality sessions per week (interval, threshold, tempo, hard hill reps, race) for recreational and mid-level runners."
evidence: "Daniels' Running Formula; Pfitzinger; broad coaching consensus."
sources:
  - literature/daniels_running_formula.md
  - literature/pfitzinger_advanced_marathoning.md
applies_to:
  population: [novice, recreational, mid_level]
computed_metric: "count(quality_sessions) per ISO week in plan/weeks/week_*.md"
status_check: "Count quality sessions in the prescribed week. If > 2, the rule fires."
---

# Two quality sessions per week, max

## Why
Recreational and mid-level runners do not have the recovery capacity of elites. Three quality sessions in a week leaves no room for adaptation; the third session reliably produces noise (or injury) rather than signal.

## What counts as quality
- Interval workouts (VO2, threshold, repetition)
- Tempo runs
- Hill reps (sustained)
- Hard fartlek
- Race or time trial
- A long run with significant fast finish (e.g., 12 mi easy + 4 mi at marathon pace counts)

What does **not** count: strides, easy hill strides, easy progression at the end of a run.

## What the coach does
- Default to one quality session for athletes <40mpw or new to structured training.
- Two quality sessions per week for established mid-level runners during build phases.
- Never three. If the athlete asks for three, push back and explain.
- Recovery weeks: drop to one quality session at most, often zero.

## When override is reasonable
- Block-periodized VO2max blocks where elite athletes do 3 quality sessions for 2–3 weeks. Not appropriate for V1's target audience.
- A race weekend that displaces the normal quality day — doesn't count as "adding" a third.

## Related rules
- `polarized_80_20` (strong_guidelines)
- `recovery_week_cadence` (strong_guidelines)
