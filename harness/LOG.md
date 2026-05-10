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

## 2026-05-10
- type: long
- distance_mi: 6.5
- duration_min: null
- avg_pace: null
- avg_hr: null
- perceived_effort: null
- sleep_hrs: null
- soreness: mild
- notes: Reported as the "long run" for the day; W19 plan called for 13 mi. Athlete reports completing all other workouts this week and feeling tired + mildly sore cumulatively over the past ~3 weeks. Location of soreness, sleep, and whether the 6.5 was a cut-short or a swap are not yet captured — to be clarified in chat.
