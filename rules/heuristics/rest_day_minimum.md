---
id: rest_day_minimum
tier: heuristic
statement: "Include at least one full rest day per week (no running, no structured training)."
evidence: "Coaching convention; recovery physiology."
sources: []
applies_to:
  population: [novice, recreational, mid_level]
computed_metric: "count(rest_days) per ISO week in plan/weeks/week_*.md"
status_check: "If a prescribed week has zero rest days, the rule fires."
---

# At least one rest day

## Why
Recovery is non-negotiable. The most common pattern in injured recreational runners is a chronic 6–7 day-per-week schedule with no full rest. Even elite athletes benefit from at least one true rest day per microcycle.

## What the coach does
- Include a rest day in every prescribed week.
- Place it the day after the hardest session of the week (typically the day after the long run, OR the day after the second quality day if those are back-to-back-ish).
- "Rest day" means no running. Walking, gentle yoga, stretching, mobility — fine. No lifting, no cross-training intervals.

## When override is reasonable
- Experienced 6-day-per-week runners with strong injury history who deliberately want a 6/0 schedule. Surface the tradeoff and let them decide.
- Recovery weeks may have 2 rest days, which is fine — more rest is not a violation.

## Related rules
- `recovery_week_cadence` (strong_guidelines)
