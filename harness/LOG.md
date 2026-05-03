# Log

Append-only run log. The coach appends entries when the athlete describes a run in chat or when an entry is parsed from `data/imports/`.

Format:

```
## YYYY-MM-DD
- type: <easy | long | interval | tempo | race | recovery | strength | cross>
- distance_mi: <number or null>
- duration_min: <number or null>
- avg_pace: <mm:ss/mi or null>
- avg_hr: <bpm or null>
- perceived_effort: <1-10 or null>
- sleep_hrs: <number or null>
- soreness: <none | mild | moderate | severe or null>
- notes: <free text from the athlete>
```

---

<!-- Entries are appended below this line, oldest first, newest last. Do not delete or rewrite past entries. -->

## 2026-04-29
- type: easy
- distance_mi: null
- duration_min: null
- avg_pace: null
- avg_hr: null
- perceived_effort: null
- sleep_hrs: null
- soreness: mild
- notes: moderate run with low-Z3 effort and a hill. 2/10 Achilles twinge during/after. Returned to baseline by next morning. Logged as Achilles monitor event in CONSTRAINTS.md.

## 2026-04-30
- type: easy
- distance_mi: 3.5
- duration_min: null
- avg_pace: null
- avg_hr: null
- perceived_effort: null
- sleep_hrs: null
- soreness: null
- notes: easy.

## 2026-05-03
- type: easy
- distance_mi: 6.25
- duration_min: null
- avg_pace: null
- avg_hr: null
- perceived_effort: null
- sleep_hrs: null
- soreness: null
- notes: easy with a 2-min Z3 pickup at the end. New 30-day max single run (was 5.5–6).
