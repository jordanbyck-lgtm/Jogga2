---
id: easy_day_hr_ceiling
tier: heuristic
statement: "Easy runs should stay below approximately 75% of max HR (or below aerobic threshold / Z2 top)."
evidence: "Coaching convention; Maffetone method (older, controversial); Seiler polarized model."
sources:
  - literature/seiler_2010_polarized.md
applies_to:
  population: [recreational, mid_level, elite]
computed_metric: "avg_hr on easy-typed runs in harness/LOG.md as fraction of max_hr from CURRENT_STATE.md"
status_check: "If recent easy runs in LOG.md show avg_hr > 0.78 * max_hr, the rule fires (athlete is running easy days too hard)."
---

# Easy day HR ceiling

## Why
The most common training failure for self-coached recreational runners is running easy days too hard. HR is the simplest objective signal that easy is actually easy.

## What the coach does
- If `harness/CURRENT_STATE.md` has max HR (measured or estimated): use 75% as a soft ceiling for easy runs, 78% as a flag.
- If recent easy runs show avg_hr above 78% of max: tell the athlete to slow down. Show them the data.
- HR drift mid-run on easy days (last mile HR > first mile HR by >10 bpm at same pace) indicates the pace was too fast or hydration/heat issues.

## When override is reasonable
- Athlete is in heat, on hills, sick, sleep-deprived — HR can be elevated for reasons unrelated to effort. Coach by RPE in those cases.
- Athlete doesn't wear a HR strap and the HR data is wrist-optical and unreliable for them — fall back to RPE and the talk test.

## Related rules
- `polarized_80_20` (strong_guidelines) — the higher-level rule this heuristic operationalizes
