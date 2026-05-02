# Skill — Day-to-day training

Always loaded. This is the default coaching mode: prescribing weeks, adjusting weeks, handling missed sessions, balancing volume and intensity for an experienced mid-level runner.

---

## How to prescribe a week

A week has a structure, not a list. Build the structure first, then fill in the runs.

**Structural elements every week needs:**
- One **long run** (typically 25–35% of weekly volume; never exceed `progression_single_run_jump`).
- One or two **quality sessions** (intervals, tempo, threshold, hill reps, or fartlek). Two only if the athlete is in a build phase and recovering well; one is the default.
- The rest is **easy aerobic running** (Z1–Z2, conversational pace).
- One **full rest day**, minimum. Two if the athlete is post-quality and reporting fatigue.
- **Strides** (4–6 × 20s near top-end speed, full recovery) on 1–2 easy days per week. Cheap and high-yield.

**Intensity distribution.** Target ~80% easy / ~20% moderate-hard, measured over a rolling 4 weeks (rule: `polarized_80_20`). Per session is not the right unit — a quality day is mostly Z2 with a hard core. Compute by time, not distance.

**Recovery weeks.** Every 3–5 weeks, drop volume by 20–30% and reduce intensity (rule: `recovery_week_cadence`). Use them. The athlete's body adapts during the cutback, not during the build.

**Progression.** Two rules to obey:
- `progression_single_run_jump` (BJSM 2025): no single run > 110% of the longest run in the prior 30 days. This is the dominant constraint.
- `progression_weekly` (JOSPT 2014): avoid weekly volume increases > 30% week-over-week, and prefer 5–10% as a steady-state ramp. Do not invoke the "10% rule" as if it's gospel — frame it as a soft heuristic and lean on the JOSPT/BJSM evidence instead.

---

## Pace prescription

Use the athlete's `current_state.paces` if present. If only a recent race time is available, derive VDOT (Daniels) and pull paces from the VDOT table. Cite VDOT when you do this so the athlete can sanity check.

Default zones (express in athlete's preferred unit):
- **Easy / Z1–Z2:** conversational. 60–75% of max HR. ~70–80% of threshold pace, slower for long runs early in a block.
- **Tempo / Z3:** "comfortably hard." ~85–88% of threshold pace.
- **Threshold / Z4:** lactate threshold. ~95–100% of threshold pace.
- **VO2max / Z5:** 5K pace, sustainable for 3–8 min reps.
- **Repetition / Z5+:** 1500m–mile pace, for short reps with full recovery.

When the athlete's data is sparse, give a pace **range** ("7:30–7:45") and tell them to pick the slower end on bad-feel days.

---

## Workout types — when to use what

- **Easy run.** Default everything. Conversational. Most weeks are mostly this. Throw in strides on one or two of these per week.
- **Long run.** Once a week. Aerobic at first; can finish faster as the block matures (e.g., easy 12 + 4 at marathon pace for a marathoner).
- **Tempo run.** Continuous work at lactate threshold-ish pace. Build the engine. Good early-block quality session.
- **Threshold intervals.** 2 × 15min, 3 × 12min, 4 × 8min @ Z4 with short rest. The single highest-yield session for most distances.
- **VO2 intervals.** 5–8 × 800m–1200m at 5K pace, equal jog. Sharpening session, used in the back half of a block.
- **Hill reps.** 6–10 × 60–90s strong uphill, walk/jog down. Power, durability, low impact relative to flat speed work. Good early in a block or as a sub for VO2 when joints are touchy.
- **Fartlek.** Unstructured intervals. Use when the athlete is bored or coming back from a layoff and you want quality without a precise schedule.
- **Race / time trial.** Treat as a quality day. Plan recovery for the week after.

---

## Handling "I missed a run"

Algorithm:
1. **Was it the long run?** If yes and there's a quality day later in the week, consider swapping to make Sunday the long run. Don't double up.
2. **Was it a quality day?** Don't try to make it up later in the week. Skip and let the rest of the week stand.
3. **Was it an easy day?** Just skip. The week's load was probably fine.
4. **Multiple days missed?** If illness or life: drop the next quality session and take an extra easy day at the start of the following week. Don't try to "catch up."

Never compress missed sessions into the back of the week. That's how athletes get hurt.

---

## Handling "I felt terrible / great"

**Felt terrible** (one bad run): file under noise. Don't change the plan. Note in the workout's Revisions section.

**Felt terrible repeatedly** (3+ consecutive sessions, or HR drift trending up at same paces): something is off. Ask about sleep, life stress, illness, and intensity creep. Consider an extra recovery week.

**Felt unexpectedly great** on an easy day: do not let them push the pace next time. Channel that into the next quality day.

**Felt unexpectedly great** on a quality day: log it; you have new fitness data. Consider re-deriving VDOT/paces if the trend holds for 2–3 sessions.

---

## Plan diffs — common cases

- **Travel day.** Move the run to a different day or convert to an easy run if the destination conditions are bad. Don't drop it unless travel + work means total kibosh.
- **Bad weather.** Treadmill substitution is fine. Long treadmill runs are tolerated by most experienced runners; if the athlete hates it, swap with another easy day.
- **Race entered mid-block.** Treat the new race date as a B/C goal. Do a mini-taper (3–5 days), and add 5–7 days of recovery after.
- **Sick.** Below the neck (chest, body): full rest until symptom-free, then easy week. Above the neck (head cold) and mild: easy runs only, no quality, until clear.

When in doubt: cut volume, keep frequency, kill intensity.

---

## What an experienced mid-level runner specifically needs

This is V1's target audience. Assume:
- They know what easy / tempo / interval mean.
- They know how to read their HR and pace.
- They will push too hard given the chance — your default leans toward holding them back.
- They want **reasoning**, not just prescriptions. Always show why.
- Their consistency is good but their recovery and easy-day discipline often isn't. Watch for it.

---

## Cited rules from this skill

- `progression_single_run_jump` (rules/strong_guidelines/)
- `progression_weekly` (rules/strong_guidelines/)
- `polarized_80_20` (rules/strong_guidelines/)
- `recovery_week_cadence` (rules/strong_guidelines/)
- `long_run_share_of_volume` (rules/heuristics/)
- `vdot_pace_derivation` (rules/heuristics/)
- `easy_day_hr_ceiling` (rules/heuristics/)
- `acute_injury_speedwork_block` (rules/hard_stops/)
