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

    python 5-machinery/scripts/loop_health.py            # human-readable
    python 5-machinery/scripts/loop_health.py --brief    # one screen, for a hook
"""

import argparse
import json
import datetime as _dt
import os
import re
import subprocess
import sys
from pathlib import Path

def _find_repo_root():
    """Repo root by MARKER, not by counting parents.

    Counting encodes this file's depth in the tree, so moving the file silently
    breaks it and no text-based check notices. Anchoring on .git survives any
    move. Added 2026-08-10 after a reorg broke three different counted idioms.
    """
    from pathlib import Path as _P
    _here = _P(__file__).resolve()
    for _p in _here.parents:
        if (_p / ".git").exists():
            return _p
    return _here.parent


REPO = _find_repo_root()
SIBLINGS = ["readers-bofm", "readers-gnt", "readers-tanakh", "readers-lxx",
            "readers-vulgate", "readers-gnt-morph", "rev-reader"]

STALE_LOG_DAYS = 30
STALE_YARDSTICK_DAYS = 45


def _git(repo: Path, *args) -> str:
    try:
        # encoding must be explicit: commit messages here carry §, em-dashes and
        # Greek, and Windows' default cp1252 decode raises on them.
        return subprocess.run(["git", *args], cwd=repo, capture_output=True,
                              text=True, encoding="utf-8", errors="replace",
                              timeout=20).stdout.strip()
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
        # The log's home keeps moving as repos reorganize: repo root originally,
        # docs/ on 2026-08-07 morning, 2-evidence/ by that afternoon. Hardcoding
        # locations produced a false "missing log" within hours, and a checker
        # that cries wolf gets ignored — the exact failure this script exists to
        # prevent. Search shallowly instead.
        log = next((p for p in sorted(repo.glob("*/retraction-log.md"))
                    if "_archive" not in p.parts and ".git" not in p.parts),
                   None)
        if (repo / "retraction-log.md").exists():
            log = repo / "retraction-log.md"
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
    # Standing default #5(c) files a cross-corpus answer to 2-evidence/ in the
    # same turn it is produced. The pre-2026-08-07 destination was
    # docs/synthesis/, which the reorg removed; checking that path reported
    # "never executed" against a loop that had in fact fired four times.
    ev = REPO / "2-evidence"
    if not ev.exists():
        return [("FAIL", "2-evidence/ does not exist — file-back has no destination")]
    pages = sorted(ev.glob("*.md"))
    if not pages:
        return [("WARN", "2-evidence/ is empty — standing default #5(c) "
                         "file-back has never executed")]
    # "Newest" is the SMALLEST age. Taking max() reported the oldest file and
    # made a loop that fired today look 9999 days stale. Uncommitted pages have
    # no git date; they are newer than anything committed, so treat them as 0.
    ages = []
    for p in pages:
        d = _days_since(_git(REPO, "log", "-1", "--format=%ad", "--date=short",
                             "--", str(p.relative_to(REPO))))
        ages.append(0 if d is None else d)
    newest = min(ages)
    return [("WARN" if newest > 30 else "ok",
             f"2-evidence/: {len(pages)} filed, newest {newest}d ago")]


def check_queue() -> list:
    q = REPO / "memories" / "operational" / "_deferred_queue.md"
    if not q.exists():
        return [("WARN", "no _deferred_queue.md")]
    age = _days_since(_git(REPO, "log", "-1", "--format=%ad", "--date=short",
                           "--", str(q.relative_to(REPO))))
    return [("WARN" if (age or 0) > 30 else "ok",
             f"deferred queue last updated {age}d ago" if age is not None
             else "deferred queue age unknown")]


STAMP = REPO / ".loop-health-last-run"
AUDIT_STAMP = REPO / ".loop-audit-last-full"

# A "move" is one commit in any tracked repo. The full hostile audit comes due on
# whichever arrives first: MOVES_DUE accumulated changes, or DAYS_DUE elapsed.
MOVES_DUE = 20
DAYS_DUE = 7


def check_audit_due() -> list:
    """Move-count trigger for the full audit (Stan's call, 2026-08-07).

    Preferred over an out-of-session scheduler. A scheduled task firing into
    genuine dormancy produces reports nobody reads until someone returns — at
    which point check_dormancy() surfaces the gap anyway. The scheduler buys an
    earlier timestamp, not earlier action. Counting moves instead fires in
    proportion to accumulated risk, needs no system-state change outside git,
    and is inspectable.

    The known limit, stated rather than hidden: like any activity trigger this
    cannot fire during silence. check_dormancy() is the other half of the pair.
    """
    since = None
    if AUDIT_STAMP.exists():
        since = _dt.datetime.fromtimestamp(AUDIT_STAMP.stat().st_mtime)
    moves, per_repo = 0, []
    for name in ["atu-method"] + SIBLINGS:
        repo = REPO.parent / name if name != "atu-method" else REPO
        if not repo.exists():
            continue
        args = ["log", "--oneline"]
        if since:
            args += [f"--since={since:%Y-%m-%dT%H:%M:%S}"]
        else:
            args += ["-30"]
        n = len([l for l in _git(repo, *args).splitlines() if l.strip()])
        if n:
            per_repo.append(f"{name} {n}")
            moves += n
    days = (_dt.datetime.now() - since).days if since else None
    due = moves >= MOVES_DUE or (days is not None and days >= DAYS_DUE)
    if since is None:
        return [("WARN", f"full audit never recorded; {moves} recent moves "
                         f"({', '.join(per_repo) or 'none'}) — run the "
                         f"atu-audit-tier skill to set the mark")]
    detail = f"{moves} moves since the last full audit ({days}d ago)"
    if per_repo:
        detail += f" [{', '.join(per_repo)}]"
    if due:
        return [("FAIL", f"AUDIT DUE — {detail}; threshold is {MOVES_DUE} moves "
                         f"or {DAYS_DUE} days. Run the atu-audit-tier skill.")]
    return [("ok", detail)]


def check_dormancy() -> list:
    """How long was the silence before this run?

    A SessionStart hook fires only when something is happening, so it is NOT the
    calendar trigger Loop 4 requires — during the six-week dormancy that lost the
    memory namespace it would have fired zero times (verified: zero commits in
    July 2026 across atu-method and all three active reader repos).

    This does not fix that. What it does is make the silence VISIBLE at the
    moment it ends: the first session back learns how long nothing was checked,
    which is the signal that was missing in June-July. A true calendar trigger
    needs an out-of-session scheduler.
    """
    out = []
    now = _dt.datetime.now()
    if STAMP.exists():
        prev = _dt.datetime.fromtimestamp(STAMP.stat().st_mtime)
        gap = (now - prev).days
        flag = "FAIL" if gap > 30 else ("WARN" if gap > 7 else "ok")
        out.append((flag, f"{gap} days since the last loop-health run "
                          f"(previous: {prev:%Y-%m-%d})"
                          + (" — a dormancy window this long is exactly when "
                             "drift accumulates unseen" if gap > 30 else "")))
    else:
        out.append(("WARN", "no prior run recorded — first run, or the stamp "
                            "was cleared"))
    try:
        STAMP.touch()
    except OSError:
        pass
    return out


def check_private_tracked() -> list:
    """Nothing under private/ may be tracked. Mechanical, because memory failed.

    private/ is gitignored in every reader repo — but .gitignore never untracks a
    file already committed, so anything added before the rule existed stays
    tracked forever and, because Pages serves from the repo root, stays PUBLIC.

    Found 2026-08-09: five files tracked across three repos, four of them
    returning HTTP 200 on live domains. The rule was right; nothing checked it.
    A folder that sits at the bottom of a listing is easy to forget, and this is
    the check that makes forgetting impossible rather than merely unlikely.
    """
    # CALIBRATION, added after this check's own first run was wrong. "Tracked
    # under private/" is NOT the failure condition — readers-lxx and
    # readers-vulgate carry `/private/*` plus `!/private/README.md`, an explicit
    # negation making that one file deliberately public. Flagging it as a leak
    # would have had Stan untracking a decision someone made on purpose.
    #
    # The real failure is a file that is tracked AND would be ignored if it
    # were not — i.e. it predates the rule and only survives because .gitignore
    # cannot untrack. `git check-ignore --no-index` distinguishes them; without
    # --no-index git skips tracked paths entirely and reports nothing, which
    # reads exactly like "no rule matches" and is the trap here.
    out, deliberate = [], 0
    for name in SIBLINGS:
        root = REPO.parent / name
        if not (root / ".git").exists():
            continue
        files = [f for f in (_git(root, "ls-files", "private") or "").splitlines()
                 if f.strip()]
        leaked = []
        for f in files:
            rule = _git(root, "check-ignore", "-v", "--no-index", f)
            if rule and ":!" not in rule.replace("\t", ""):
                leaked.append(f)          # matched by a positive rule → accident
            elif rule:
                deliberate += 1           # matched by a `!` negation → intended
        if leaked:
            shown = ", ".join(x[len("private/"):] for x in leaked[:3])
            out.append(("FAIL", f"{name}: {len(leaked)} file(s) tracked under "
                                f"private/ that .gitignore would otherwise "
                                f"exclude — live if Pages serves the root ({shown})"))
    if not out:
        out.append(("ok", f"private/ clean — 0 accidental, "
                          f"{deliberate} deliberately un-ignored"))
    return out


def refresh_log() -> list:
    """Regenerate the derived operations log. Runs every session, unprompted.

    The hand-written log.md was built 2026-08-09 and was ten commits stale by
    that evening. Deriving it from git removes the failure mode rather than
    warning about it — there is no "remember to update the log" step left.
    """
    script = REPO / "5-machinery/scripts" / "build_log.py"
    if not script.exists():
        return [("WARN", "build_log.py missing — log.md is hand-written again")]
    r = subprocess.run([sys.executable, str(script)], cwd=REPO,
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=60)
    msg = (r.stdout or "").strip().splitlines()[-1:] or ["no output"]
    return [("ok" if r.returncode == 0 else "FAIL", f"log: {msg[0]}")]


def check_lessons_capture() -> list:
    """Corrections happened; were any written down?

    lessons.md has a PROMOTION trigger but had no CAPTURE trigger, and the gap
    showed: on 2026-08-09 two failures — a miscalibrated private/ check and a
    .gitignore commit that silently did not land — went uncaptured while the
    file sat at zero open entries.

    The mechanical signal is correction-shaped commits since lessons.md last
    changed. A commit saying `fix:` or `correct:` is a correction by its own
    account; if none of them produced a lesson, the buffer is not being fed.
    Heuristic, and deliberately loud rather than clever.
    """
    f = REPO / "4-process" / "lessons.md"
    if not f.exists():
        return [("WARN", "lessons.md missing — no capture buffer")]
    since = _git(REPO, "log", "-1", "--format=%aI", "--", "4-process/lessons.md")
    if not since:
        return [("ok", "lessons.md never committed yet")]
    log = _git(REPO, "log", f"--since={since}", "--format=%s")
    corrections = [ln for ln in (log or "").splitlines()
                   if re.match(r"^(fix|correct|revert|untrack|security):", ln)]
    if not corrections:
        return [("ok", "no uncaptured corrections since lessons.md last changed")]
    shown = corrections[0][:60]
    return [("WARN", f"{len(corrections)} correction commit(s) since lessons.md "
                     f"last changed, 0 captured — e.g. \"{shown}\"")]


def check_lessons() -> list:
    """Unpromoted lessons are worry-beads — so give promotion a mechanical trigger.

    4-process/lessons.md exists because capturing a correction is not learning it;
    promotion into CLAUDE.md or a guard is. That promotion step is the bearing of
    the whole ops loop, and it has no trigger — which is how the file becomes the
    thing it was built to prevent.

    Demonstrated 2026-08-09: I wrote lessons.md with five entries, declared
    promotion "the audit's job", and then did not run the audit in the same
    session. Stan had to ask. A rule with no trigger is a rule nobody applies —
    the same defect as a detector with no calibration.
    """
    f = REPO / "4-process" / "lessons.md"
    if not f.exists():
        return [("WARN", "4-process/lessons.md missing — no capture buffer")]
    text = f.read_text(encoding="utf-8", errors="replace")
    # Count ONLY what sits under "## Open" — stop at the next H2. The first
    # version counted every "### [" heading in the file and so read the five
    # ARCHIVED captures as open, reporting 6 the moment one real item arrived.
    # A checker that cannot tell open from closed is the same defect as a
    # checker with no known-bad case; caught 2026-08-09, one hour after
    # promoting "a detector is itself a claim" into CLAUDE.md #6.
    open_n, in_open = 0, False
    for ln in text.splitlines():
        if ln.startswith("## "):
            in_open = ln.startswith("## Open")
            continue
        if in_open and ln.startswith("### [") and "~~" not in ln:
            open_n += 1
    if not open_n:
        return [("ok", "lessons.md: nothing awaiting promotion")]
    age = _days_since(_git(REPO, "log", "-1", "--format=%ad", "--date=short",
                           "--", "4-process/lessons.md"))
    flag = "WARN" if (open_n >= 5 or (age or 0) > 14) else "ok"
    return [(flag, f"lessons.md: {open_n} captured, 0 promoted"
                   f"{f' (oldest touch {age}d ago)' if age is not None else ''}"
                   f"{' — promotion has no trigger; run the audit' if flag == 'WARN' else ''}")]


def check_pointers() -> list:
    # 5-machinery/ is readers-bofm's layout, not this repo's; the path was
    # copied across and reported "missing" against a script that exists.
    script = REPO / "5-machinery/scripts" / "check_broken_pointers.py"
    if not script.exists():
        return [("WARN", f"{script.relative_to(REPO).as_posix()} missing")]
    r = subprocess.run([sys.executable, str(script)], cwd=REPO,
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=120)
    def grab(label):
        m = re.search(label + r":\s+(\d+)", r.stdout or "")
        return m.group(1) if m else "?"
    anchors, paths, wiki = (grab("broken anchors"), grab("broken doc paths"),
                            grab("broken wikilinks"))
    # Anchors and wikilinks are strict: both classes are ones we created and can
    # keep at zero. Doc paths carry known external/retired noise, so they report.
    flag = "FAIL" if {anchors, wiki} - {"0", "?"} else "ok"
    return [(flag, f"pointers: {anchors} broken anchors, {wiki} broken "
                   f"wikilinks, {paths} broken doc paths")]


def check_current_tasks() -> list:
    """Current-Tasks.md is RETIRED. Check that it stays a pointer, not a board.

    It was always meant to die. Its own header: "it is the seed for the GitHub
    Project board — when that exists, this file is retired rather than
    maintained alongside it." The board went live 2026-08-09 with 16 items.

    The drift check that used to live here was correct and kept firing — 23
    commits behind on 2026-08-11 — but it was measuring the wrong thing. Chasing
    that warning by updating the file would have restored the exact defect the
    board was built to end: two places to look for pending work, disagreeing.
    Stan's words: "the problem has been you have had lots of places to hide the
    pending things; if there's only one place to look, I'll be able to catch up."

    So the check inverts. Staleness is now EXPECTED and silent. What is reported
    is the file growing back into a board — because that, not age, is the
    failure. The board itself is not checkable from here; it lives in GitHub and
    `gh` may be absent or unauthenticated, so this deliberately verifies the
    local half only and says so.
    """
    board = REPO / "Current-Tasks.md"
    if not board.exists():
        return [("ok", "Current-Tasks.md retired — board is the single surface")]
    text = board.read_text(encoding="utf-8", errors="replace")
    # A pointer is short and names the board. A board has task structure:
    # checkboxes, or many headed sections.
    checkboxes = len(re.findall(r"^\s*[-*]\s*\[[ xX]\]", text, re.M))
    sections = len(re.findall(r"^#{2,3}\s", text, re.M))
    points_at_board = bool(re.search(r"projects?/1\b|colometry-project|Project board",
                                     text, re.I))
    if checkboxes or sections > 3:
        return [("WARN", f"Current-Tasks.md has regrown into a board "
                         f"({checkboxes} checkboxes, {sections} sections) — "
                         f"pending work belongs on the project board, not here")]
    if not points_at_board:
        return [("WARN", "Current-Tasks.md is retired but does not point at the board")]
    return [("ok", "Current-Tasks.md is a pointer to the board, as intended")]


def in_family(cwd: str) -> bool:
    """Is the invoking directory part of this program's repo family?

    Family, not repo: a readers-bofm session SHOULD open knowing atu-method's
    state, which is the whole point of the cross-repo checks. So the gate admits
    atu-method, every entry in SIBLINGS, and biblical-corpora.
    """
    if not cwd:
        return False
    norm = cwd.replace("\\", "/").lower()
    names = ["atu-method", "biblical-corpora", *SIBLINGS]
    return any(f"/{n}" in norm or norm.endswith(n) for n in (x.lower() for x in names))


def _hook_cwd() -> str:
    """Read the invoking directory Claude Code passes as JSON on stdin.

    Same shape as ~/.claude/hooks/check_bash_discipline.py, which already does
    `data = json.loads(sys.stdin.read())` then `data.get("cwd", "")`. Copied
    rather than reinvented.

    Returns "" when there is no stdin payload — i.e. a human ran the script by
    hand — and a hand run is never gated.
    """
    if sys.stdin is None or sys.stdin.isatty():
        return ""
    try:
        raw = sys.stdin.read()
    except Exception:
        return ""
    if not raw.strip():
        return ""
    try:
        return (json.loads(raw) or {}).get("cwd", "") or ""
    except Exception:
        return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brief", action="store_true")
    args = ap.parse_args()

    # SCOPE GATE. This script is registered as a USER-level SessionStart hook, so
    # it runs in every workspace on the machine — and it reports on atu-method
    # plus SIBLINGS regardless of where it was called from, because REPO anchors
    # on the script's own location and nothing ever read the caller's directory.
    #
    # The cost was never tokens. turkish-wiki resumed from a compaction, received
    # nine findings about reader-repo baselines, and correctly answered "not this
    # workspace — ignoring it." Training unrelated sessions to ignore
    # SessionStart output, at a compaction resume when context is scarcest, is
    # how an alarm stops working everywhere. Silent exit, because a "not
    # applicable here" message is still noise.
    #
    # Same category error as a project skill in the global bucket: the test is
    # "does this serve every workspace, or one family?"
    # An EMPTY cwd means no hook payload — a human ran this by hand — and a hand
    # run is never gated. Only gate when we actually received a directory and it
    # is outside the family. Getting this backwards silenced the family repos
    # and the hand run too, which is a worse failure than the noise it fixes.
    _cwd = _hook_cwd()
    if args.brief and _cwd and not in_family(_cwd):
        return 0

    sections = [
        ("dormancy since last check", check_dormancy),
        ("full-audit due? (move-count trigger)", check_audit_due),
        ("retraction -> promotion loop", check_retraction_logs),
        ("validator baselines", check_baselines),
        ("outcome instrument (gold yardstick)", check_yardstick),
        ("file-back loop", check_fileback),
        ("private/ tracking", check_private_tracked),
        ("deferred queue", check_queue),
        ("current-tasks board", check_current_tasks),
        ("log (derived)", refresh_log),
        ("lessons <- capture", check_lessons_capture),
        ("lessons -> promotion", check_lessons),
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
        print("  (full: python 5-machinery/scripts/loop_health.py)")
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
