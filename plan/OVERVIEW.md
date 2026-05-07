# Plan overview

## Block purpose
26-week buildup to **NYC Marathon, Sun 2026-11-01**.
A goal: **sub-3:00** (6:51 /mi). B: 3:05. C: 3:10. Decision point: half tune-up Sat 2026-09-05.

Durability bias throughout. Achilles is the limiting tissue; posterior-chain weakness and hamstring history are secondary risks. Volume ceiling intentionally moderate (~47 mpw peak) to protect tissue.

## Block duration
- start_week: 2026-W19 (Mon 2026-05-04)
- end_week: 2026-W44 (race week, Sun 2026-11-01)
- total_weeks: 26 (W19 through W44 inclusive)

## Mesocycle structure
- **W19–W26 (8 wk) — Base rebuild.** 19 → 28 mpw. 1 quality (sub-threshold) per week. Long run 6 → 12 mi. Strides 2x/wk. Hill strides introduced W23. Cutbacks W22 and W26.
- **W27–W30 (4 wk) — Early build.** 30 → 36 mpw. Add a true second quality (threshold intervals). Long run 12 → 16. Cutback W30.
- **W31–W39 (9 wk) — Marathon-specific build.** 38 → 45 mpw. MP segments enter long runs. Threshold + MP work as the two quality sessions. Cutback W34. Half tune-up W36 (Sep 5). Cutback-style week post-half W37 if needed.
- **W40–W44 (5 wk) — Peak + 3-week taper.**
  - W40: build week, 45 mpw, 18 mi LR with MP segments.
  - W41: peak week, 47 mpw, 22 mi LR with MP segments (peak LR 3 weeks pre-race).
  - W42: taper 1, ~38 mpw (−20%), 1 threshold + MP LR 16.
  - W43: taper 2, ~28 mpw (−40%), 1 short threshold, LR 12 (4 MP).
  - W44: race week. Race Sun Nov 1.

## Weekly totals (sketch — unlocked weeks revisable)
| ISO Wk | Dates | Phase | Volume (mi) | Long run (mi) | Quality |
| ------ | --- | --- | ---: | ---: | --- |
| W19 | May 4–10 | Base 1 | 19 | 6 | 1 ST (intro, 4×3 min) |
| W20 | May 11–17 | Base 2 | 22 | 6.5–7 | 1 ST (4×4 min) |
| W21 | May 18–24 | Base 3 | 24 | 8 | 1 ST + 30-min field test |
| W22 | May 25–31 | Cutback | 19 | 6 | 1 ST light |
| W23 | Jun 1–7 | Base 4 | 25 | 9 | 1 ST + hill strides |
| W24 | Jun 8–14 | Base 5 | 27 | 10 | 1 ST + hill strides |
| W25 | Jun 15–21 | Base 6 | 28 | 11 | 1 ST + hill strides |
| W26 | Jun 22–28 | Cutback / 10K race week | 22 | (10K race or 7) | 10K time trial OR 1 ST |
| W27 | Jun 29–Jul 5 | Build 1 | 30 | 12 | 1 ST + 1 threshold |
| W28 | Jul 6–12 | Build 2 | 32 | 13 | 1 ST + 1 threshold |
| W29 | Jul 13–19 | Build 3 | 34 | 14 | 1 ST + 1 threshold |
| W30 | Jul 20–26 | Cutback | 28 | 11 | 1 quality |
| W31 | Jul 27–Aug 2 | Specific 1 | 36 | 14 (3 MP) | 1 thresh + 1 MP segment LR |
| W32 | Aug 3–9 | Specific 2 | 38 | 16 (4 MP) | 1 thresh + MP LR |
| W33 | Aug 10–16 | Specific 3 | 40 | 17 (5 MP) | 1 thresh + MP LR |
| W34 | Aug 17–23 | Cutback | 32 | 13 | 1 thresh |
| W35 | Aug 24–30 | Specific 4 | 42 | 18 (6 MP) | 1 thresh + MP LR |
| W36 | Aug 31–Sep 6 | Tune-up week | 36 | HM tune-up Sep 5 (~13.1) | HM @ MP-effort |
| W37 | Sep 7–13 | Recovery from HM | 32 | 12 | 1 easy quality |
| W38 | Sep 14–20 | Specific 5 | 42 | 18 (8 MP) | 1 thresh + MP LR |
| W39 | Sep 21–27 | Specific 6 | 45 | 20 (8 MP) | 1 thresh + MP LR |
| W40 | Sep 28–Oct 4 | Build | 45 | 18 (6 MP) | 1 thresh + MP LR |
| W41 | Oct 5–11 | Peak | 47 | 22 (8 MP) | 1 thresh + MP LR |
| W42 | Oct 12–18 | Taper 1 | 38 | 16 | 1 thresh + small MP |
| W43 | Oct 19–25 | Taper 2 | 28 | 12 (4 MP) | 1 short threshold |
| W44 | Oct 26–Nov 1 | Race week | 18 + race | RACE Sun | shake-out + strides only |

Cutback cadence: every 4th week (W22, W26, W30, W34, W38).

## Quality session evolution
- **W19–W22:** 1 ST (sub-threshold) per week. Effort-based (Z3 ceiling, RPE 6–7), short intervals (3–4 min reps with 1 min jog). NOT pace-pinned because paces will recalibrate post-field-test and post-10K.
- **W21:** 30-min field test (W19's twinge has 3 weeks to settle; volume has stabilized). Updates LTHR and threshold pace.
- **W23–W26:** 1 ST + 1 set of **hill strides** (8–10 × 10–12s on a moderate incline, walk down). Low Achilles eccentric load, neuromuscular benefit, transferable to NYCM hills.
- **W27–W30:** 1 ST + 1 threshold (continuous tempo or longer reps at LT pace). True second quality.
- **W31–W39:** 1 threshold + 1 MP-specific session. MP first appears as segments embedded in the long run, then progresses to MP intervals.
- **W40–W44:** Cut to 1 quality. Maintain intensity, slash volume.

## Long run progression (with constraints)
- 30-day max single run as of 2026-05-03 = 6.25 mi (today's run). All long-run prescriptions check `progression_single_run_jump` (≤110% of 30-day max).
- 6 → 22 mi over 22 progression long runs (excluding cutbacks and races). Avg growth ~0.7 mi per progression run. Well under 10% cap throughout.
- MP segments enter at W31 — small (3 mi) and grow to 8 mi by W39.

## Pace targets (current — will recalibrate after W21 field test and June 10K)
Athlete-supplied estimates from HM HR data:
- E (easy): 8:30–9:30 /mi (HR 145–162)
- ST (sub-threshold): 6:55–7:05 — **defer pace-pinning until W21 test; use Z3 effort + HR cap (168–176) until then**
- T (threshold): 6:35–6:45
- I (5K pace / VO2): 6:05–6:20
- M (goal MP): 6:51 (sub-3:00) / 7:04 (3:05) / 7:15 (3:10)
- R (repetition): 5:45–5:55

## Risk flags
1. **Achilles** — recurring tendinopathy, twinge 2026-04-29 (2/10, resolved by AM). All speedwork that loads Achilles eccentrically (true intervals, fast-finish LRs) deferred until W22+ AND 2 weeks symptom-free. `acute_achilles_no_speedwork` rule active monitor; fires if AM stiffness >5–10 min, sharp pain, or swelling.
2. **Hamstring history** — 2 prior strains. No cold sprints. Nordic curls 2x/wk ongoing per Lift B/C.
3. **Volume rebuild** — current 14–15 mpw to 47 mpw peak = 3x. Cutbacks every 4th week mandatory. Watch for HR drift on easy days.
4. **Goal pace gap** — sub-3:00 requires +5 VDOT from PR fitness. If W36 half is not ≥1:25, recalibrate to 3:05 / 3:10. Athlete already aligned on this.
5. **Sub-38 10K (June)** — aspirational. Holding plan structure regardless of 10K result; we'll use it as data, not a failure mode.
6. **47 mpw ceiling** — low for sub-3:00. Honest tradeoff for durability. Reassessment point at W36 half.

## Field test plan (W21, May 18–24)
- 30-min all-out continuous time trial on a flat route. Ideally Wed of W21 if Achilles is silent.
- Measures: avg HR for 30 min ≈ LTHR. Avg pace ≈ ~T pace + ~5–10 sec/mi (Daniels approximation).
- If anything hurts: abort, log, no retest until symptom-free.
