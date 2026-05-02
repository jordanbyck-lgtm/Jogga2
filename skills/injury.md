# Skill — Injury management (STUB)

Loaded on triggers: "pain", "hurt", "ache", "sore" (when not just from a hard workout), "injury", "injured", "tweak", "PT", "physio", "doctor", "imaging", or any specific anatomy ("Achilles", "plantar", "ITB", "knee", "shin", "hip flexor", etc.).

This skill is a stub at V1. The hard-stop rules in `rules/hard_stops/` are the active safety layer. When this skill is triggered, do the following:

## V1 minimum

1. **Always lead with the disclaimer.** "Not medical advice. If you suspect a serious injury, see a sports medicine doc or PT."
2. **Severity triage** (your best LLM judgment):
   - **Mild discomfort, no functional limitation:** modify the next 2–3 sessions — drop intensity, swap quality for easy, add an extra rest day. Note in `harness/CONSTRAINTS.md`.
   - **Pain that changes gait or persists at rest:** stop running. Recommend PT consult. Gate further running prescriptions until the athlete reports cleared or improved.
   - **Acute trauma, sudden onset, sharp pain, swelling, can't bear weight:** stop running immediately. Recommend urgent care or sports med. No prescription until medical sign-off.
3. **Check hard stops.** Specifically:
   - `rules/hard_stops/return_to_run_post_stress_fracture.md` if there's any history of stress fracture in the area.
   - `rules/hard_stops/acute_achilles_no_speedwork.md` for Achilles symptoms.
   - `rules/hard_stops/chest_pain_full_stop.md` for cardiac symptoms.
4. **Modify the plan.** Use the plan-diff workflow. Justification should reference the symptom and the conservative bias.
5. **Log to `harness/CONSTRAINTS.md`.** Append the new symptom with date, location, severity, and what action was taken.

## When to escalate to "see a professional"

When in doubt, escalate. Specific triggers:
- Pain on weight-bearing rest
- Pain that wakes the athlete at night
- Pain > 7 days despite training reduction
- Numbness, tingling, weakness
- Visible swelling, bruising, or deformity
- Any chest pain, dizziness, or syncope (cardiac)
- Pain in the same spot recurring across multiple cycles

## Cited rules from this skill

- `acute_injury_speedwork_block` (rules/hard_stops/)
- `return_to_run_post_stress_fracture` (rules/hard_stops/)
- `acute_achilles_no_speedwork` (rules/hard_stops/)
- `chest_pain_full_stop` (rules/hard_stops/)
