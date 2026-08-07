#!/usr/bin/env python3
"""Loop health — mechanical staleness checks across the improvement loops.

This is the automation half of the audit tier. The tier as first written was a
note asking a future session to remember to run something, which is the exact
failure that lost the memory namespace: the tool existed, no cadence ran it. A
hook runs this; nobody has to remember.

Every check answers "is a loop still turning?" with a date or a count, never an
opinion. Fast by design (no repo walks beyond globs) so it can fire at
SessionStart without being felt.

Checks:
  1. Retraction->promotion loop  — per reader repo: log present? last entry?
                                   any DISCIPLINE PROMOTED block ever?
  2. Validator baselines         — baseline older than the newest corpus/parse
                                   commit means the gate has stopped controlling.
  3. Gold yardstick age          — the only outcome instrument; if it is stale,
                                   no loop can be shown to improve anything.
  4. File-back loop              — docs/synthesis/ empty means default #5(c) has
                                   never executed.
  5. Deferred-queue stalls       — items flagged pending for too long.
  6. Pointer integrity           — delegates to check_broken_pointers.py.

Exit code is always 0: this reports, it does not block. Blocking belongs to
pre-commit gates, which sit next to the corpus they protect.

    python scripts/loop_health.py            # human-readable
    python scripts/loop_health.py --brief    # one screen, for a hook
"""

import argparse
import datetime as _dt
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SIBLINGS = ["readers-bofm", "readers-gnt", "readers-tanakh", "readers-lxx",
            "readers-vulgate", "readers-gnt-morph", "rev-reader"]

STALE_LOG_DAYS = 30
STALE_YARDSTICK_DAYS = 45


def _git(repo: Path, *args) -> str:
    try:
        return subprocess.run(["git", *args], cwd=repo, capture_output=True,
                              text=True, timeout=20).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def _days_since(stamp: str) -> int | None:
    try:
        d = _dt.date.fromisoformat(stamp[:10])
    except ValueError:
        return None
    return (_dt.date.today() - d).days


def check_retraction_logs() -> list:
    out = []
    for name in SIBLINGS:
        repo = REPO.parent / name
        if not repo.exists():
            continue
        # Repo-root was the original convention; readers-bofm moved its log to
        # docs/ on 2026-08-07. Look in both rather than reporting a false
        # "missing log" — a checker that cries wolf gets ignored, which is the
        # failure mode this whole script exists to prevent.
        log = next((p for p in (repo / "retraction-log.md",
                                repo / "docs" / "retraction-log.md")
                    if p.exists()), None)
        if log is None:
            out.append(("WARN", f"{name}: no retraction-log.md"))
            continue
        text = log.read_text(encoding="utf-8", errors="replace")
        entries = len(re.findall(r"^### \d{4}-", text, re.M))
        promos = len(re.findall(r"^## .*DISCIPLINE PROMOTED", text, re.M))
        last = _git(repo, "log", "-1", "--format=%ad", "--date=short", "--",
                    str(log.relative_to(repo)).replace(os.sep, "/"))
        age = _days_since(last) if last else None
        flag = "WARN" if (age is not None and age > STALE_LOG_DAYS) else "ok"
        out.append((flag, f"{name}: {entries} entries, {promos} promotions, "
                          f"last touched {last or 'unknown'}"
                          + (f" ({age}d ago)" if age is not None else "")))
    total_promos = sum(int(re.search(r"(\d+) promotions", m[1]).group(1))
                       for m in out if "promotions" in m[1])
    if total_promos == 0 and any("entries" in m[1] for m in out):
        out.append(("FAIL", "retraction->promotion loop has NEVER fired: "
                            "entries accumulate, zero promotions corpus-wide"))
    return out


def check_baselines() -> list:
    out = []
    for name in SIBLINGS:
        repo = REPO.parent / name
        base = repo / "validators" / ".baseline.json"
        if not base.exists():
            continue
        b_date = _git(repo, "log", "-1", "--format=%ad", "--date=short", "--",
                      "validators/.baseline.json")
        c_date = _git(repo, "log", "-1", "--format=%ad", "--date=short", "--",
                      "data/")
        if b_date and c_date and b_date < c_date:
            out.append(("FAIL", f"{name}: baseline {b_date} predates newest "
                                f"corpus/parse commit {c_date} — the gate has "
                                f"stopped controlling; counts drift is "
                                f"accumulated intentional change, not decay"))
        elif b_date:
            out.append(("ok", f"{name}: baseline {b_date} current"))
    return out


def check_yardstick() -> list:
    hits = list((REPO.parent).glob("readers-*/private/substrate/**/"
                                   "*gold-yardstick*.json"))
    if not hits:
        return [("WARN", "no gold yardstick found — no outcome instrument")]
    out = []
    for h in hits:
        age = (_dt.date.today()
               - _dt.date.fromtimestamp(os.path.getmtime(h))).days
        flag = "WARN" if age > STALE_YARDSTICK_DAYS else "ok"
        out.append((flag, f"{h.parent.parent.parent.name}: yardstick last "
                          f"modified {age}d ago"))
    return out


def check_fileback() -> list:
    syn = REPO / "docs" / "synthesis"
    if not syn.exists():
        return [("WARN", "docs/synthesis/ does not exist — standing default "
                         "#5(c) file-back has never executed")]
    n = len(list(syn.glob("*.md")))
    return [("WARN" if n == 0 else "ok",
             f"docs/synthesis/: {n} pages")]


def check_queue() -> list:
    q = REPO / "memories" / "operational" / "_deferred_queue.md"
    if not q.exists():
        return [("WARN", "no _deferred_queue.md")]
    age = _days_since(_git(REPO, "log", "-1", "--format=%ad", "--date=short",
                           "--", str(q.relative_to(REPO))))
    return [("WARN" if (age or 0) > 30 else "ok",
             f"deferred queue last updated {age}d ago" if age is not None
             else "deferred queue age unknown")]


def check_pointers() -> list:
    script = REPO / "scripts" / "check_broken_pointers.py"
    if not script.exists():
        return [("WARN", "check_broken_pointers.py missing")]
    r = subprocess.run([sys.executable, str(script)], cwd=REPO,
                       capture_output=True, text=True, timeout=120)
    m = re.search(r"broken anchors:\s+(\d+)", r.stdout or "")
    anchors = m.group(1) if m else "?"
    m2 = re.search(r"broken doc paths:\s+(\d+)", r.stdout or "")
    paths = m2.group(1) if m2 else "?"
    flag = "FAIL" if anchors not in ("0", "?") else "ok"
    return [(flag, f"pointers: {anchors} broken anchors, {paths} broken doc paths")]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brief", action="store_true")
    args = ap.parse_args()

    sections = [
        ("retraction -> promotion loop", check_retraction_logs),
        ("validator baselines", check_baselines),
        ("outcome instrument (gold yardstick)", check_yardstick),
        ("file-back loop", check_fileback),
        ("deferred queue", check_queue),
        ("pointer integrity", check_pointers),
    ]

    findings = []
    for title, fn in sections:
        try:
            rows = fn()
        except Exception as e:                      # never break a session
            rows = [("WARN", f"check failed: {e.__class__.__name__}: {e}")]
        findings.append((title, rows))

    bad = [(t, m) for t, rows in findings for f, m in rows if f in ("FAIL", "WARN")
           for t in [t]]

    if args.brief:
        if not bad:
            print("loop-health: all checks ok")
            return 0
        print(f"loop-health: {len(bad)} item(s) need attention")
        for t, m in bad[:8]:
            print(f"  - {m}")
        print("  (full: python scripts/loop_health.py)")
        return 0

    print("=" * 72)
    print("Loop health — are the improvement loops still turning?")
    print("=" * 72)
    for title, rows in findings:
        print(f"\n{title}")
        for flag, msg in rows:
            mark = {"ok": "  ok  ", "WARN": " WARN ", "FAIL": " FAIL "}[flag]
            print(f"  [{mark}] {msg}")
    print("\nThis reports; it does not block. Blocking gates live next to the "
          "corpus they protect.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
