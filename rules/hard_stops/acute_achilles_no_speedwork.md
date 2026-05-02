---
id: acute_achilles_no_speedwork
tier: hard_stop
statement: "No speedwork (intervals, tempo, hill reps, strides) while the athlete reports active acute Achilles symptoms."
evidence: "Silbernagel et al., clinical management of Achilles tendinopathy."
sources:
  - literature/silbernagel_achilles_management.md
applies_to:
  population: [all]
  conditions: [acute_achilles_pain, achilles_tendinopathy_flare]
computed_metric: "Mention of acute Achilles pain in last 14 days in harness/LOG.md or harness/CONSTRAINTS.md."
status_check: "If LOG.md or recent chat mentions Achilles pain that is sharp, swollen, painful at rest, or new-onset within 14 days, this rule fires."
---

# Acute Achilles flare — no speedwork

Speedwork loads the Achilles eccentrically and at high force. Pushing through an acute flare causes tendon damage and chronic tendinopathy.

## When this fires
- Sharp Achilles pain during or immediately after a run
- Swelling, warmth, or visible thickening of the tendon
- Pain on first steps in the morning that doesn't ease in 5–10 minutes
- Pain at rest

Note: chronic mild Achilles tightness without these features is a different scenario — load management still matters but this specific rule does not fire.

## What the coach does
1. Remove all speedwork from upcoming sessions until symptoms resolve.
2. Reduce volume by 30–50% until pain on weight-bearing has cleared.
3. Recommend isometric calf holds (e.g., 5 × 45s holds, mid-range) as a tolerated load. Progress to slow heel raises only as pain allows.
4. Recommend PT consult if symptoms persist >7 days or worsen.
5. Log to `harness/CONSTRAINTS.md`.

## Override
Athlete can request to keep easy running if pain is not present at rest and gait is unchanged. Speedwork itself does **not** allow override during an acute flare. If the athlete insists on speedwork, restate the risk and refuse to write the prescription.

## Related rules
- `return_to_run_post_stress_fracture` (rules/hard_stops/) — broader injury hard stop
