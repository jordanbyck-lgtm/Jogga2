# Plan overview

## Block purpose
23-week buildup to Chicago Marathon 2026 (Sun 2026-10-11). Goal: sub-3:20 (7:38/mi). Stretch: sub-3:18.

## Block duration
- start_week: 2026-W18 (week of 2026-04-27, partial — starting Sat 2026-05-02)
- end_week: 2026-W41 (race week, Sun 2026-10-11)
- total_weeks: 23 (W18 through W41 inclusive)

## Mesocycle structure
- **W18–W22 (5 wk) — Base rebuild.** 30 → 40 mpw. 1 quality session/wk (fartlek → tempo). Long run 12 → 14. Reintroduce strides + eccentric calf maintenance.
- **W23–W26 (4 wk) — Endurance.** 42 → 48 mpw. Add a midweek medium-long run. Long run 14 → 18. 1 quality.
- **W27 — Recovery week.** ~36 mpw. No second quality.
- **W28–W31 (4 wk) — Lactate threshold.** 45 → 50 mpw. 2 quality (LT continuous + LT intervals; medium-long with MP segments). Long run 18 → 20.
- **W32 — Recovery week.** ~38 mpw.
- **W33–W35 (3 wk) — Race specific.** 48 → 52 mpw. MP-segment long runs. 2 quality. Half-marathon tune-up race in W34 (target ~1:35 ≈ VDOT 51).
- **W36 — Recovery week.** ~40 mpw.
- **W37–W38 (2 wk) — Peak.** 53–55 mpw. Last 20-mile long run in W37.
- **W39–W40 (2 wk) — Taper.** Volume −20% then −40%. Maintain quality intensity, cut volume. Last hard session ~10 days out.
- **W41 — Race week.** ~25 mpw + race Sun 10/11.

## Weekly totals (sketch)
| ISO Wk | Phase | Volume (mi) | Long run (mi) | Quality |
| ------ | ----- | ----------: | ------------: | ------- |
| W18 | Base (partial) | ~17 | 12 | none |
| W19 | Base | 36 | 13 | fartlek 6×1 |
| W20 | Base | 38 | 14 | fartlek 8×1 |
| W21 | Base | 40 | 12 (cutback) | tempo 4 mi |
| W22 | Base | 40 | 14 | tempo 4 mi |
| W23 | Endurance | 42 | 15 | tempo 5 mi |
| W24 | Endurance | 45 | 16 | LT 2×2 mi |
| W25 | Endurance | 47 | 17 | LT 4×1 mi |
| W26 | Endurance | 48 | 18 | LT 2×2.5 mi |
| W27 | Recovery | 36 | 13 | tempo 3 mi |
| W28 | LT focus | 45 | 18 | LT 5 mi continuous |
| W29 | LT focus | 48 | 19 | LT 2×3 mi |
| W30 | LT focus | 50 | 20 | LT 6 mi continuous |
| W31 | LT focus | 50 | 18 (cutback) | LT 3×2 mi |
| W32 | Recovery | 38 | 13 | tempo 4 mi |
| W33 | Specific | 48 | 19 (4 @ MP) | MP intervals |
| W34 | Specific | 45 | tune-up HM (~13.1) | HM race |
| W35 | Specific | 52 | 20 (8 @ MP) | LT 2×3 mi |
| W36 | Recovery | 40 | 14 | tempo 4 mi |
| W37 | Peak | 53 | 20 (10 @ MP) | LT 6 mi + MP int. |
| W38 | Peak | 55 | 18 (8 @ MP) | LT 4×1.5 mi |
| W39 | Taper | 44 | 14 | LT 3×1.5 mi |
| W40 | Taper | 32 | 10 (4 @ MP) | LT 2×1 mi |
| W41 | Race | 25 + race | RACE | none pre-race |

## Key milestone weeks
- **W21, W27, W32, W36** — recovery weeks (volume −20–30%, intensity reduced)
- **W34** — half-marathon tune-up race (used to update VDOT and goal pace)
- **W37** — peak long run (20 mi with 10 @ MP)
- **W41** — race

## Pace targets (current, will update post-tune-up)
Derived from current VDOT 46 (recent 22:30 5K) — these will revise upward as fitness rebuilds:
- E (easy): 8:30–9:00 /mi
- M (marathon, current fitness): 7:55 /mi
- M (goal pace, race): 7:38 /mi
- T (threshold): 7:30 /mi (current); ~7:00 /mi at peak fitness (VDOT 51)
- I (intervals, 5K pace): 7:14 /mi (current); ~6:35 /mi at peak fitness
- R (repetition): not in current prescription

## Risk flags
1. Achilles history (resolved 2023). Eccentric calf maintenance scheduled 2x/wk through the block. Any flare → `acute_achilles_no_speedwork` rule fires immediately, plan pivots.
2. 6 days/wk + work + protected Friday = no buffer. Bias rest decisions conservatively.
3. Volume nearly doubles over the block (30 → 55). Recovery weeks placed every 4–5 weeks to manage.
4. Goal pace requires +16 sec/mi over PR. The W34 tune-up half is the decision point: if it doesn't suggest VDOT 50+, dial goal back to 3:25.
