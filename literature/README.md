# Literature

Curated sources the coach can cite. Allowlist-only. Each source is a markdown file with metadata frontmatter and a notes body.

## Allowlist (V1)

- Daniels, Jack. *Daniels' Running Formula* (3rd ed.)
- Pfitzinger, Pete & Douglas, Scott. *Advanced Marathoning* (3rd ed.)
- Magness, Steve. *The Science of Running*
- Fitzgerald, Matt. *80/20 Running*
- Hadd ("Hadd's Approach to Distance Running"). Letsrun forum compendium.
- Karp, Jason R. Various peer-reviewed work and books.
- Seiler, Stephen. Peer-reviewed work on polarized training.
- Mujika, Iñigo. Peer-reviewed work on tapering and periodization.

## Allowlisted journals

- *British Journal of Sports Medicine* (BJSM)
- *Journal of Orthopaedic & Sports Physical Therapy* (JOSPT)
- *Medicine & Science in Sports & Exercise* (MSSE)
- *Sports Medicine* (Springer)
- *International Journal of Sports Physiology and Performance* (IJSPP)
- *European Journal of Applied Physiology*

## Denylist

- General-interest running blogs (Runner's World, Outside, Trail Runner) without specific peer-reviewed citation
- Coach Twitter/Instagram opinion threads
- AI-generated content
- Influencer book promotions without underlying study citations
- Anything attributed to "studies show" without a specific named study

## Tagging conventions

In each source file's frontmatter:

```yaml
---
title: "<source title>"
authors: ["<surname, first initial>"]
year: <yyyy>
type: book | rct | cohort | meta_analysis | review | expert_opinion | clinical_practice
evidence_tier: high | medium | low
populations:
  - novice | recreational | mid_level | elite
  - age_band: [<min>, <max>]   # optional
  - sex: any | male | female   # optional
topics: [periodization, polarized, vdot, taper, injury_prevention, ...]
training_phases: [base, build, peak, taper, recovery, return_to_run]
injury_subtypes: [achilles_tendinopathy, bone_stress, itb_syndrome, ...]   # if applicable
---
```

## How the coach uses these

- When making a training-science claim, cite by `title` + `year` and link to the file.
- When asked "is X evidence-backed?", read the relevant `literature/*.md` files (use Explore subagents in parallel for >2 sources) and report what the sources actually say, including any conflicts.
- Rules in `rules/` reference these files directly. Don't break those references when editing.

## V1 seed set

Seven sources are seeded at V1:
- `daniels_running_formula.md`
- `pfitzinger_advanced_marathoning.md`
- `seiler_2010_polarized.md`
- `bjsm_2025_single_run_progression.md`
- `jospt_2014_weekly_progression.md`
- `mujika_2003_taper.md`
- `silbernagel_achilles_management.md`
- `warden_2014_bone_stress_injuries.md`

These are notes, not full ingestions. Real ingestion (chunking, vector indexing, full-text retrieval) is deferred to a later version. For V1, the coach reads these notes directly and uses web search to fill gaps.
