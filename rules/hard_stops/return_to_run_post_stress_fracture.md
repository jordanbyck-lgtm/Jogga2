---
id: return_to_run_post_stress_fracture
tier: hard_stop
statement: "After a confirmed bone stress injury, no running until cleared by a sports medicine professional, then follow a graded walk-jog progression."
evidence: "Clinical consensus; Warden et al. JOSPT 2014 on bone stress injury management."
sources:
  - literature/warden_2014_bone_stress_injuries.md
applies_to:
  population: [all]
  conditions: [post_stress_fracture, suspected_stress_fracture]
computed_metric: "Presence of stress fracture / BSI in last 6 months in harness/CONSTRAINTS.md without medical clearance noted."
status_check: "If CONSTRAINTS.md mentions a stress fracture or BSI within the last 6 months and no clearance note, this rule fires for any running prescription."
---

# Return to run post stress fracture

Bone heals on its own timeline. Push too early and you re-injure or convert a stress reaction to a full fracture.

## When this fires
- Athlete reports a current or recent (within 6 months) stress fracture, BSI, stress reaction, or "hot spot" on imaging.
- Athlete reports localized bony pain on percussion, single-leg hop, or weight-bearing rest, without medical evaluation.

## What the coach does
1. Refuse running prescriptions until the athlete confirms medical clearance (PT, sports med doc, or orthopedist).
2. Recommend non-impact cross-training (cycling, pool running, elliptical) to maintain aerobic fitness.
3. Once cleared, follow a graded walk-jog progression. Typical pattern: weeks 1–2 walking only, weeks 3–4 walk-jog intervals (1 min jog / 4 min walk progressing), then short continuous easy runs every other day.
4. Re-establish baseline volume gradually before reintroducing any quality work.

## Override
This rule **does not allow override** without explicit medical clearance. If the athlete pushes back, restate the risk and hold the line.

## Related rules
- `acute_injury_speedwork_block` (rules/hard_stops/) — no speedwork during return-to-run progression
- `progression_single_run_jump` (rules/strong_guidelines/) — applies once running resumes
