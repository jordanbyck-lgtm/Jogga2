"""Parse a run-data export (.gpx, .fit, .csv) and emit a LOG.md entry to stdout.

V1: scaffolded but UNTESTED. The athlete will validate manually first; this code
path comes online later. The coach (Claude Code) can call this via Bash:

    python3 scripts/parse_export.py data/imports/<file>

It prints a LOG.md-formatted entry to stdout. The coach is responsible for
deciding whether to append it (e.g., to ask the athlete first about effort,
sleep, soreness — fields the file format can't supply).

Supported formats:
  - .csv   — Strava activity export (Activity Data) or generic CSV with columns
             date, type, distance_mi, duration_min, avg_pace, avg_hr
  - .gpx   — track points; computes distance and duration; pace and HR if present
  - .fit   — Garmin/Wahoo binary; requires `fitparse` (pip install fitparse)

Notes:
  - This is a starter implementation, not battle-tested. Edge cases (multi-segment
    GPX, paused timers, GPS dropouts) will need polish.
  - On any parse failure the script prints a clear error to stderr and exits 1.
  - Effort, sleep, soreness fields are emitted as `null` — the file can't supply them.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


GPX_NS = {"gpx": "http://www.topografix.com/GPX/1/1"}


def haversine_mi(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R_mi = 3958.7613
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R_mi * math.asin(math.sqrt(a))


def fmt_pace(pace_min_per_mi: float | None) -> str:
    if pace_min_per_mi is None or pace_min_per_mi <= 0 or math.isinf(pace_min_per_mi):
        return "null"
    minutes = int(pace_min_per_mi)
    seconds = int(round((pace_min_per_mi - minutes) * 60))
    if seconds == 60:
        minutes += 1
        seconds = 0
    return f"{minutes}:{seconds:02d}/mi"


def parse_gpx(path: Path) -> dict:
    tree = ET.parse(path)
    root = tree.getroot()
    pts: list[tuple[float, float, datetime, float | None, int | None]] = []
    for trkpt in root.iter("{http://www.topografix.com/GPX/1/1}trkpt"):
        lat = float(trkpt.attrib["lat"])
        lon = float(trkpt.attrib["lon"])
        time_el = trkpt.find("gpx:time", GPX_NS)
        ele_el = trkpt.find("gpx:ele", GPX_NS)
        hr = None
        ext = trkpt.find("gpx:extensions", GPX_NS)
        if ext is not None:
            for child in ext.iter():
                tag = child.tag.split("}")[-1].lower()
                if tag in ("hr", "heartrate") and child.text:
                    try:
                        hr = int(float(child.text))
                    except ValueError:
                        pass
        if time_el is None or time_el.text is None:
            continue
        ts = datetime.fromisoformat(time_el.text.replace("Z", "+00:00"))
        ele = float(ele_el.text) if (ele_el is not None and ele_el.text) else None
        pts.append((lat, lon, ts, ele, hr))
    if len(pts) < 2:
        raise ValueError("GPX has no usable track points")

    distance_mi = 0.0
    for (lat1, lon1, _, _, _), (lat2, lon2, _, _, _) in zip(pts, pts[1:]):
        distance_mi += haversine_mi(lat1, lon1, lat2, lon2)
    duration_s = (pts[-1][2] - pts[0][2]).total_seconds()
    duration_min = duration_s / 60
    pace = duration_min / distance_mi if distance_mi > 0 else None
    hrs = [p[4] for p in pts if p[4] is not None]
    avg_hr = int(sum(hrs) / len(hrs)) if hrs else None
    return {
        "date": pts[0][2].astimezone(timezone.utc).date().isoformat(),
        "distance_mi": round(distance_mi, 2),
        "duration_min": round(duration_min, 1),
        "avg_pace": fmt_pace(pace),
        "avg_hr": avg_hr,
    }


def parse_fit(path: Path) -> dict:
    try:
        from fitparse import FitFile
    except ImportError as e:
        raise RuntimeError(
            "Parsing .fit requires `fitparse`. Install with: pip install fitparse"
        ) from e

    fit = FitFile(str(path))
    distance_m = 0.0
    duration_s = 0.0
    hrs: list[int] = []
    start_time: datetime | None = None
    for record in fit.get_messages("session"):
        for f in record:
            if f.name == "total_distance" and f.value is not None:
                distance_m = float(f.value)
            elif f.name == "total_timer_time" and f.value is not None:
                duration_s = float(f.value)
            elif f.name == "avg_heart_rate" and f.value is not None:
                hrs.append(int(f.value))
            elif f.name == "start_time" and f.value is not None:
                start_time = f.value
    if distance_m == 0 or duration_s == 0:
        raise ValueError("FIT file missing session totals")
    distance_mi = distance_m / 1609.344
    duration_min = duration_s / 60
    pace = duration_min / distance_mi if distance_mi > 0 else None
    return {
        "date": (start_time or datetime.now(timezone.utc)).date().isoformat(),
        "distance_mi": round(distance_mi, 2),
        "duration_min": round(duration_min, 1),
        "avg_pace": fmt_pace(pace),
        "avg_hr": hrs[0] if hrs else None,
    }


def parse_csv(path: Path) -> dict:
    """Strava bulk export 'activities.csv' or generic single-row CSV."""
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        raise ValueError("CSV is empty")
    row = rows[0]

    def get(*keys: str, default: str = "") -> str:
        for k in keys:
            for actual in row:
                if actual.lower().strip() == k.lower():
                    return (row[actual] or "").strip()
        return default

    date_str = get("date", "Activity Date", "start_time")
    try:
        date = datetime.fromisoformat(date_str.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        try:
            date = datetime.strptime(date_str, "%b %d, %Y, %I:%M:%S %p").date().isoformat()
        except ValueError:
            date = datetime.now(timezone.utc).date().isoformat()

    def to_float(s: str) -> float | None:
        s = s.strip()
        if not s:
            return None
        try:
            return float(s)
        except ValueError:
            return None

    distance_mi = to_float(get("distance_mi"))
    if distance_mi is None:
        # Strava export "Distance" is in km
        d_km = to_float(get("Distance", "distance_km", "distance"))
        distance_mi = round(d_km / 1.609344, 2) if d_km is not None else None

    duration_min = to_float(get("duration_min"))
    if duration_min is None:
        # Strava export "Moving Time" is in seconds
        d_s = to_float(get("Moving Time", "duration_s", "elapsed_time"))
        duration_min = round(d_s / 60, 1) if d_s is not None else None

    avg_pace_str = get("avg_pace")
    if not avg_pace_str and distance_mi and duration_min:
        avg_pace_str = fmt_pace(duration_min / distance_mi)
    if not avg_pace_str:
        avg_pace_str = "null"

    avg_hr = to_float(get("avg_hr", "Average Heart Rate"))
    avg_hr_int = int(avg_hr) if avg_hr is not None else None

    return {
        "date": date,
        "distance_mi": distance_mi if distance_mi is not None else "null",
        "duration_min": duration_min if duration_min is not None else "null",
        "avg_pace": avg_pace_str,
        "avg_hr": avg_hr_int if avg_hr_int is not None else "null",
    }


def emit_log_entry(parsed: dict, run_type: str = "easy") -> str:
    return (
        f"## {parsed['date']}\n"
        f"- type: {run_type}\n"
        f"- distance_mi: {parsed['distance_mi']}\n"
        f"- duration_min: {parsed['duration_min']}\n"
        f"- avg_pace: {parsed['avg_pace']}\n"
        f"- avg_hr: {parsed['avg_hr']}\n"
        f"- perceived_effort: null\n"
        f"- sleep_hrs: null\n"
        f"- soreness: null\n"
        f"- notes: parsed from file import; ask athlete for effort/sleep/soreness\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="Parse a run export to a LOG.md entry")
    ap.add_argument("path", help="Path to .gpx, .fit, or .csv file")
    ap.add_argument("--type", default="easy", help="Run type tag (default: easy)")
    args = ap.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"error: file not found: {path}", file=sys.stderr)
        return 1

    suffix = path.suffix.lower()
    try:
        if suffix == ".gpx":
            parsed = parse_gpx(path)
        elif suffix == ".fit":
            parsed = parse_fit(path)
        elif suffix == ".csv":
            parsed = parse_csv(path)
        else:
            print(f"error: unsupported file type: {suffix}", file=sys.stderr)
            return 1
    except Exception as e:
        print(f"error: failed to parse {path}: {e}", file=sys.stderr)
        return 1

    print(emit_log_entry(parsed, run_type=args.type))
    return 0


if __name__ == "__main__":
    sys.exit(main())
