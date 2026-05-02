---
id: polarized_80_20
tier: strong_guideline
statement: "Approximately 80% of weekly training time should be at low intensity (Z1–Z2) and 20% at moderate-to-high intensity (Z3 and above), measured over a rolling 4 weeks by time, not distance."
evidence: "Seiler 2010 — polarized training in elite endurance athletes; replicated in recreational populations."
sources:
  - literature/seiler_2010_polarized.md
applies_to:
  population: [recreational, mid_level, elite]
computed_metric: "ratio of (time in Z1+Z2) to (time in Z3+Z4+Z5) across the rolling last 4 weeks of harness/LOG.md"
status_check: "Compute easy/hard time split from LOG.md over last 4 weeks. If easy share < 75% the rule fires (training is too intense). If easy share > 90% over multiple weeks the rule does not fire but flag low intensity exposure."
---

# 80/20 polarized intensity distribution

## Why
The single most consistent finding across endurance training literature: athletes who keep most of their volume genuinely easy and concentrate hard work in dedicated sessions improve faster and stay healthier than athletes who run "moderate" most of the time.

## What "easy" means
"Easy" means conversational, Z2 or below, with HR comfortably under aerobic threshold. The classic failure mode is **moderate-pace junk** — too hard to be recovery, too easy to be quality. The coach should be aggressive about pulling athletes off this pace.

## What the coach does
- Track time-in-zone (or pace-band proxy) across the rolling 4 weeks.
- Target: 75–85% of total time at easy / Z1–Z2.
- If the athlete's recent weeks have crept to 70/30 or worse: pull intensity back. Convert one quality session per week to easy + strides.
- Measure by **time, not distance**. Easy miles take longer than hard miles, so distance-based ratios systematically understate easy share.

## When override is reasonable
- Race-week and tune-up weeks where the volume is intentionally redistributed.
- During a deliberate VO2max block where intensity is concentrated for 3–4 weeks before a recovery cut.
- For very low-volume athletes (<20mpw), the rule is less pressure-tested in research and easy/hard ratios become noisy.

## Per-session note
80/20 is a **rolling 4-week measurement**, not a per-session rule. A quality day will be 50/50 easy/hard within that day. Don't compute the ratio per session.

## Related rules
- `recovery_week_cadence` (strong_guidelines) — recovery weeks naturally bias toward easy
- `easy_day_hr_ceiling` (heuristics) — operational guidance for keeping easy days actually easy
