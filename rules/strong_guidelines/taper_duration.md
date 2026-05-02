---
id: taper_duration
tier: strong_guideline
statement: "Taper duration scales with race distance: ~7 days for 5K/10K, 10–14 days for half marathon, 14–21 days for marathon and longer."
evidence: "Mujika & Padilla 2003 meta-analysis on taper structure; Pfitzinger marathon plans."
sources:
  - literature/mujika_2003_taper.md
  - literature/pfitzinger_advanced_marathoning.md
applies_to:
  population: [novice, recreational, mid_level, elite]
computed_metric: "days from peak training week to goal race date in plan/OVERVIEW.md"
status_check: "If a goal race is identified in GOALS.md, check that the taper window in the plan matches the race distance. If shorter than the recommended window, the rule fires."
---

# Taper duration

## Why
Tapering reduces accumulated fatigue while preserving fitness. The science (Mujika & Padilla meta-analysis) finds that:
- Volume reductions of 40–60% over the taper window produce the largest performance gains.
- Intensity should be **maintained** during taper — keep some quality, reduce its volume.
- Frequency should largely be maintained (don't take suddenly more rest days).

Too short a taper leaves residual fatigue. Too long a taper produces detraining.

## Distance-specific guidance
- **5K / 10K:** 7-day mini-taper. Cut volume ~30%. Last hard session ~5 days out.
- **Half marathon:** 10–14 day taper. Volume reduces 30–40% in the first taper week, 50% in race week.
- **Marathon:** 2–3 week taper. Volume reduces 20% → 40% → 60% across the three weeks. Last long run 2–3 weeks out, max ~75% of peak long run.
- **Ultra (50K+):** Taper similar to marathon, sometimes extended to 3–4 weeks for very long events.

## What the coach does
- When laying out the goal-race block, count back from race date to set the taper window.
- Mark taper weeks in `plan/OVERVIEW.md`.
- Maintain key intensity in taper sessions; cut their volume.

## When override is reasonable
- Athlete has a strong personal preference based on prior data. Don't fight a taper structure that has worked.
- Tune-up race during a build block: use a 3–5 day mini-taper, not the full distance-appropriate one.

## Related rules
- `recovery_week_cadence` (strong_guidelines)
- `long_run_share_of_volume` (heuristics)
