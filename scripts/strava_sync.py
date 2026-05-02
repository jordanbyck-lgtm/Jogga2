"""Sync recent Strava activities into a local LOG.md-formatted preview.

V1: scaffolded but UNTESTED. Activated later when the athlete is ready to wire up
Strava. The webhook pathway is NOT included here — webhooks need a public URL,
which V1 doesn't have. This script polls Strava's /athlete/activities on demand.

Usage:
    # First time: register a Strava API app at https://www.strava.com/settings/api
    # Then export your client ID and secret:
    export STRAVA_CLIENT_ID=...
    export STRAVA_CLIENT_SECRET=...

    # Authorize (opens browser):
    python3 scripts/strava_sync.py auth

    # Pull recent activities and emit LOG.md-formatted entries:
    python3 scripts/strava_sync.py pull --since 2025-04-01

Tokens are cached in data/strava/tokens.json (gitignored).

The coach (Claude Code) can call this via Bash and decide whether to append
the output to harness/LOG.md.
"""

from __future__ import annotations

import argparse
import http.server
import json
import os
import socketserver
import sys
import time
import urllib.parse
import urllib.request
import webbrowser
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TOKENS_PATH = REPO_ROOT / "data" / "strava" / "tokens.json"
CALLBACK_HOST = "127.0.0.1"
CALLBACK_PORT = 53682
SCOPE = "read,activity:read"


def _load_tokens() -> dict | None:
    if not TOKENS_PATH.exists():
        return None
    return json.loads(TOKENS_PATH.read_text())


def _save_tokens(tokens: dict) -> None:
    TOKENS_PATH.parent.mkdir(parents=True, exist_ok=True)
    TOKENS_PATH.write_text(json.dumps(tokens, indent=2))


def _exchange_code(client_id: str, client_secret: str, code: str) -> dict:
    data = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "grant_type": "authorization_code",
        }
    ).encode()
    req = urllib.request.Request("https://www.strava.com/oauth/token", data=data)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def _refresh(client_id: str, client_secret: str, refresh_token: str) -> dict:
    data = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        }
    ).encode()
    req = urllib.request.Request("https://www.strava.com/oauth/token", data=data)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def _ensure_access_token(client_id: str, client_secret: str) -> str:
    tokens = _load_tokens()
    if tokens is None:
        raise RuntimeError("No tokens. Run `python3 scripts/strava_sync.py auth` first.")
    if tokens.get("expires_at", 0) - 60 < time.time():
        new = _refresh(client_id, client_secret, tokens["refresh_token"])
        _save_tokens(new)
        return new["access_token"]
    return tokens["access_token"]


def cmd_auth() -> int:
    client_id = os.environ.get("STRAVA_CLIENT_ID")
    client_secret = os.environ.get("STRAVA_CLIENT_SECRET")
    if not client_id or not client_secret:
        print(
            "error: STRAVA_CLIENT_ID and STRAVA_CLIENT_SECRET must be set in env",
            file=sys.stderr,
        )
        return 1

    redirect_uri = f"http://{CALLBACK_HOST}:{CALLBACK_PORT}/callback"
    auth_url = (
        "https://www.strava.com/oauth/authorize?"
        + urllib.parse.urlencode(
            {
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "response_type": "code",
                "approval_prompt": "auto",
                "scope": SCOPE,
            }
        )
    )

    captured: dict = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            parsed = urllib.parse.urlparse(self.path)
            qs = urllib.parse.parse_qs(parsed.query)
            if parsed.path == "/callback" and "code" in qs:
                captured["code"] = qs["code"][0]
                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Strava authorized. You can close this tab.")
            else:
                self.send_response(400)
                self.end_headers()

        def log_message(self, *args, **kwargs) -> None:
            return

    print(f"Opening browser to authorize Strava: {auth_url}")
    webbrowser.open(auth_url)

    with socketserver.TCPServer((CALLBACK_HOST, CALLBACK_PORT), Handler) as httpd:
        httpd.timeout = 1
        deadline = time.time() + 300
        while "code" not in captured and time.time() < deadline:
            httpd.handle_request()
        if "code" not in captured:
            print("error: timed out waiting for Strava authorization", file=sys.stderr)
            return 1

    tokens = _exchange_code(client_id, client_secret, captured["code"])
    _save_tokens(tokens)
    print(f"Tokens saved to {TOKENS_PATH}")
    return 0


def _activity_to_log_entry(act: dict) -> str:
    start = act.get("start_date_local") or act.get("start_date")
    date = (
        datetime.fromisoformat(start.replace("Z", "+00:00")).date().isoformat()
        if start
        else datetime.now(timezone.utc).date().isoformat()
    )
    type_raw = (act.get("type") or "").lower()
    workout_type = act.get("workout_type")
    if type_raw not in ("run", "trailrun", "virtualrun"):
        run_type = "cross"
    elif workout_type == 2:
        run_type = "long"
    elif workout_type == 3:
        run_type = "interval"
    elif workout_type == 1:
        run_type = "race"
    else:
        run_type = "easy"

    distance_m = act.get("distance") or 0
    distance_mi = round(distance_m / 1609.344, 2) if distance_m else "null"
    moving_s = act.get("moving_time") or 0
    duration_min = round(moving_s / 60, 1) if moving_s else "null"
    if isinstance(distance_mi, float) and isinstance(duration_min, float) and distance_mi > 0:
        pace_min = duration_min / distance_mi
        m = int(pace_min)
        s = int(round((pace_min - m) * 60))
        if s == 60:
            m += 1
            s = 0
        avg_pace = f"{m}:{s:02d}/mi"
    else:
        avg_pace = "null"
    avg_hr = int(act["average_heartrate"]) if act.get("average_heartrate") else "null"
    name = (act.get("name") or "").replace("\n", " ")

    return (
        f"## {date}\n"
        f"- type: {run_type}\n"
        f"- distance_mi: {distance_mi}\n"
        f"- duration_min: {duration_min}\n"
        f"- avg_pace: {avg_pace}\n"
        f"- avg_hr: {avg_hr}\n"
        f"- perceived_effort: null\n"
        f"- sleep_hrs: null\n"
        f"- soreness: null\n"
        f"- notes: synced from Strava — \"{name}\"; ask athlete for effort/sleep/soreness\n"
    )


def cmd_pull(args: argparse.Namespace) -> int:
    client_id = os.environ.get("STRAVA_CLIENT_ID")
    client_secret = os.environ.get("STRAVA_CLIENT_SECRET")
    if not client_id or not client_secret:
        print(
            "error: STRAVA_CLIENT_ID and STRAVA_CLIENT_SECRET must be set in env",
            file=sys.stderr,
        )
        return 1

    access = _ensure_access_token(client_id, client_secret)

    params = {"per_page": 50}
    if args.since:
        after_dt = datetime.fromisoformat(args.since)
        params["after"] = int(after_dt.replace(tzinfo=timezone.utc).timestamp())

    url = "https://www.strava.com/api/v3/athlete/activities?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access}"})
    with urllib.request.urlopen(req) as resp:
        activities = json.loads(resp.read().decode())

    if not activities:
        print("no activities found", file=sys.stderr)
        return 0

    for act in activities:
        print(_activity_to_log_entry(act))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Strava sync (poll, no webhook)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("auth", help="Run localhost OAuth flow")
    pull = sub.add_parser("pull", help="Fetch recent activities and emit LOG.md entries")
    pull.add_argument("--since", help="ISO date (YYYY-MM-DD); only activities after this", default=None)
    args = ap.parse_args()

    if args.cmd == "auth":
        return cmd_auth()
    if args.cmd == "pull":
        return cmd_pull(args)
    return 1


if __name__ == "__main__":
    sys.exit(main())
