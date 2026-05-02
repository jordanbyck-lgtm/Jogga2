# Jogga

A chat-first agentic running coach. V1 is a CLI dogfood: Claude Code itself is the agent.

## Run it

```bash
claude
```

Run `claude` from this repo's root. The `CLAUDE.md` at the root turns the session into Jogga. There is no other UI at V1.

Talk to it in plain language:
- `let's get started` — first run, walks onboarding
- `show me this week` / `what's tomorrow` — surfaces the calendar from `plan/weeks/`
- `did 8mi at 7:45 avg, felt easy, slept poorly` — appends to `harness/LOG.md`
- `I'm traveling Friday, can you adjust this week` — produces a plan diff with a justification

## Layout

- `CLAUDE.md` — the agent's runtime contract (system prompt)
- `ONBOARDING.md` — ~10 question seed set, every question skippable
- `harness/` — persistent state about the athlete (read/written by the agent)
- `plan/` — the prescribed training plan; one markdown file per week
- `skills/` — domain skills loaded on demand (day-to-day is full; rest are stubs at V1)
- `rules/` — the rules engine: hard stops, strong guidelines, heuristics
- `literature/` — curated source notes the agent cites
- `data/` — `imports/` for file-drop run data; `strava/` for OAuth tokens (deferred)
- `scripts/` — `parse_export.py` and `strava_sync.py` (scaffolded but not tested at V1)

## Audit log

Git history is the audit log. Plan diffs, log appends, and rule violations all land as commits — readable, attributable, reversible. Run `git log -p` after a session to review.

## Out of scope at V1

Web frontend, FastAPI backend, Postgres, Firebase Auth, Strava webhook, deterministic Python rule computation, eval harness, multi-user. See `/root/.claude/plans/jogga-project-fancy-seal.md` for the V1 plan and the deferred items.
