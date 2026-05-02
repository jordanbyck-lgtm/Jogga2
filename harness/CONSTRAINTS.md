# Constraints

<!--
Anything that bounds the plan: schedule, equipment, terrain, climate, travel,
injuries (active and historical). Coach reads this every turn.
-->

## Weekly availability
- days_available:           # e.g., Mon, Tue, Wed, Thu, Sat, Sun
- protected_days:           # rest enforced
- typical_run_window:       # morning / lunch / evening
- typical_run_duration_cap: # how much time they have on a normal day
- long_run_day:

## Schedule variability
<!-- Travel, work cycles, family commitments that shift week to week. -->

## Active injuries
<!--
Append entries here as the athlete reports issues, with date, location,
severity, and what action was taken.
Format:
## YYYY-MM-DD — <location>
- severity: <mild | moderate | severe>
- description: <what it feels like>
- action: <what the coach changed in the plan>
- resolved: <YYYY-MM-DD or "not yet">
-->

## Historical injuries
<!-- Anything that put them out for >2 weeks. Stress fractures especially. -->

## Equipment
- shoes_in_rotation:
- gps_watch:
- hr_strap:
- treadmill_access:
- gym_access:

## Environment
- typical_terrain:          # road | trail | track | mixed
- climate:
- altitude:
- access_to_track:
- access_to_pool:
