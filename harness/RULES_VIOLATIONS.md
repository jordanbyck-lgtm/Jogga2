# Rules violations

Append-only log. The coach appends an entry every time it delivers advice that deviates from a `strong_guideline` rule (or a `heuristic` deviation that is more than incidental).

Hard-stop rules are not "violated" in the same sense — they require explicit athlete acknowledgment to override and are logged here only when the athlete has acknowledged.

Format:

```
## YYYY-MM-DD HH:MM
- rule_id: <id from rules/>
- tier: <hard_stop | strong_guideline | heuristic>
- what_was_recommended: <one line>
- justification: <one paragraph; why deviating from the rule was the right call>
- athlete_acknowledged: <yes | not_required>
- outcome: <to be filled in later if relevant>
```

---

<!-- Entries are appended below this line, oldest first, newest last. Do not delete or rewrite past entries. -->
