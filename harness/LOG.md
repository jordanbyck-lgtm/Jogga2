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
