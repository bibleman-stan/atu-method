#!/usr/bin/env python3
"""Find prose damaged by the five-tier reorg's path rewrite.

WHY THIS EXISTS. The 2026-08-10 reorg rewrote directory names without a leading
word boundary, so bare English nouns became paths wherever they appeared:

    "no code, no canon, no rule"      -> "no code, no 1-method/canon, no rule"
    "persistent scripts under"        -> "persistent 5-machinery/scripts under"
    r"BCE|CE|AD|BC|test|tests|second" -> r"...|test|5-machinery/tests|second"

The third was a live break: that is a regex ALTERNATION of bare words, so the
alternative "tests" stopped matching anything. Fourteen instances were found and
fixed in readers-tanakh on 2026-08-11, and then two more turned up in
atu-method/1-method/framework.md -- in the canon itself, in the sentence
describing the two punctuation-invariant syntactic tests.

DETECTION. A grep for the prefix cannot work: "5-machinery/scripts" is a real
directory in most repos and a mangle only in prose. Two signals separate them:

  1. Does the path RESOLVE in the repo it appears in? `1-method/canon` is real
     in readers-tanakh and fictional in atu-method.
  2. Is it marked up as a path? Legitimate references sit in backticks or
     markdown links. Prose mangles are bare.

Neither alone is sufficient -- a real directory named in bare prose is still a
mangle, and an unresolvable path in backticks is a broken link rather than this
defect -- so both are reported, scored, and the caller judges.

    python detect_reorg_mangles.py --calibrate
    python detect_reorg_mangles.py                 # all repos
    python detect_reorg_mangles.py readers-gnt     # one repo
"""

import argparse
import os
import re
import sys

REPOS = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

PREFIXES = ["1-method", "2-evidence", "3-project", "3-implementation",
            "4-process", "5-machinery"]

# prefix/word, where word does NOT continue into a deeper path segment.
# Must allow sentence punctuation after the word: an earlier lookahead excluded
# any following "." and so could not see a mangle that ended a sentence.
PAT = re.compile(r"(?<![\w/.-])(" + "|".join(PREFIXES) + r")/([a-z_][a-z0-9_-]*)"
                 r"(?![\w-])(?!/)(?!\.[A-Za-z0-9])")

SKIP_DIRS = ("_archive", "_old", ".archive", "__pycache__", ".git",
             "node_modules", "books", "data")
EXTS = (".md", ".py", ".html", ".json", ".txt", ".sh")


def marked_up(line: str, start: int, end: int) -> bool:
    """True if the match sits in backticks or a markdown link target."""
    before, after = line[:start], line[end:]
    if before.count("`") % 2 == 1:
        return True
    if before.rstrip().endswith("](") or before.rstrip().endswith("]("):
        return True
    if re.search(r"\]\([^)]*$", before):
        return True
    # a bare path immediately followed by / or a filename is a real reference
    return bool(re.match(r"^/", after))


def scan(repo: str):
    """Yield (relpath, lineno, matched, resolves, marked, line)."""
    root = os.path.join(REPOS, repo)
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in files:
            if not fn.endswith(EXTS):
                continue
            full = os.path.join(dirpath, fn)
            try:
                lines = open(full, encoding="utf-8", errors="replace").read().splitlines()
            except OSError:
                continue
            for i, line in enumerate(lines, 1):
                for m in PAT.finditer(line):
                    token = m.group(0)
                    resolves = os.path.exists(os.path.join(root, token))
                    yield (os.path.relpath(full, root), i, token,
                           resolves, marked_up(line, m.start(), m.end()), line.strip())


def calibrate() -> bool:
    """Poles on the pattern. The known-bad ones matter most: a false positive
    here invites an edit to prose that was already correct."""
    ok = True
    cases = [
        ("no code, no 1-method/canon, no rule", True, "bare noun rewritten as a path"),
        ("persistent 5-machinery/scripts under", True, "bare plural rewritten"),
        (r'r"BCE|CE|AD|BC|test|5-machinery/tests|second"', True, "inside a regex alternation"),
        ("see 5-machinery/scripts/build_log.py for detail", False,
         "real file path is NOT flagged"),
        ("lives in 5-machinery/validators/colometry/", False,
         "real directory path with trailing slash is NOT flagged"),
        ("the atu-method/1-method/framework.md canon", False,
         "repo-qualified path is NOT flagged"),
        ("plain prose about canon and validators", False,
         "unprefixed words are NOT flagged"),
    ]
    for text, want, why in cases:
        got = bool(PAT.search(text))
        hit = got == want
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why}", file=sys.stderr)
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repos", nargs="*")
    ap.add_argument("--calibrate", action="store_true")
    ap.add_argument("--all", action="store_true", help="include resolving+marked-up hits")
    args = ap.parse_args()

    if args.calibrate:
        print("calibration -- flag rewritten prose, never a real path", file=sys.stderr)
        ok = calibrate()
        print("\nCALIBRATED" if ok else "\nMISCALIBRATED", file=sys.stderr)
        return 0 if ok else 1

    if not calibrate():
        print("MISCALIBRATED -- refusing to report", file=sys.stderr)
        return 1
    print()

    targets = args.repos or [d for d in sorted(os.listdir(REPOS))
                             if os.path.isdir(os.path.join(REPOS, d, ".git"))]
    grand = 0
    for repo in targets:
        rows = list(scan(repo))
        # A mangle is bare prose. Marked-up hits are links (broken or not);
        # resolving+bare is still suspect but far more likely legitimate.
        suspect = [r for r in rows if not r[4]] if not args.all else rows
        if not suspect:
            print(f"  {repo}: clean")
            continue
        print(f"  {repo}: {len(suspect)} suspect")
        for rel, ln, tok, res, mk, line in suspect[:40]:
            flag = "resolves" if res else "NO-SUCH-PATH"
            print(f"      {rel}:{ln}  {tok}  [{flag}]")
            print(f"          {line[:110]}")
        if len(suspect) > 40:
            print(f"      ... +{len(suspect)-40} more")
        grand += len(suspect)
    print(f"\n  total suspect: {grand}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
