#!/usr/bin/env python3
"""Strip reorg-inserted path prefixes off bare English nouns.

Companion to detect_reorg_mangles.py. The 2026-08-10 five-tier reorg rewrote
directory names with no leading word boundary, so every bare occurrence of
"canon", "validators", "scripts", "tests" in prose acquired a path prefix:

    "defensible against the canon"  ->  "defensible against the 1-method/canon"
    "producer validators don't"     ->  "producer 5-machinery/validators don't"
    r"...|test|tests|second|..."    ->  r"...|test|5-machinery/tests|second|..."

The fix is to remove the prefix, restoring the noun.

THE DANGEROUS CASE, and why the preposition guard exists. Some bare occurrences
are legitimate references to the directory itself:

    "the scripts live in 5-machinery/scripts"

Stripping that yields "live in scripts", which is wrong. Any occurrence
preceded by a locative preposition -- in / at / under / from / to / see /
within / inside -- is left alone. That is deliberately conservative: leaving a
real mangle unfixed is visible and cheap, while corrupting a correct path
reference is neither.

Also skipped: anything in backticks or a markdown link (those are real
references), and anything continuing into a deeper path segment.

    python fix_reorg_mangles.py --calibrate
    python fix_reorg_mangles.py --check <repo>...    # dry run
    python fix_reorg_mangles.py <repo>...            # rewrite
"""

import argparse
import os
import re
import sys

REPOS = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

PREFIXES = ["1-method", "2-evidence", "3-project", "3-implementation",
            "4-process", "5-machinery"]
# The lookahead must reject a real path continuation while ALLOWING sentence
# punctuation. An earlier version excluded any following "." and therefore could
# not see a single mangle that ended a sentence -- calibration caught it before
# it rewrote anything, which is the entire point of the poles.
PAT = re.compile(r"(?<![\w/.-])(" + "|".join(PREFIXES) + r")/([a-z_][a-z0-9_-]*)"
                 r"(?![\w-])(?!/)(?!\.[A-Za-z0-9])")

# Locative prepositions: the word after these names a location, so the path is real.
GUARD = re.compile(r"\b(in|at|under|from|to|see|within|inside|into|via|of)\s+$", re.I)

SKIP_DIRS = ("_archive", "_old", ".archive", "__pycache__", ".git",
             "node_modules", "books", "data")

# MARKDOWN PROSE ONLY. The first version of this script also rewrote .py, .json
# and .sh, and corrupted path-mapping tables in the reorg tooling:
#
#     ("5-machinery/scripts", "5-machinery/scripts") -> ("scripts", "scripts")
#     "scholarship": "2-evidence/scholarship"        -> "scholarship": "scholarship"
#
# The preposition guard could not help: a quoted string literal has no English
# grammar around it. Every calibration pole was a sentence, so every pole passed
# while code silently broke. Prose is the only context where "the prefix is
# wrong" can be decided from surrounding words, so prose is the only context
# this script touches. The handful of genuine .py cases are fixed by hand.
EXTS = (".md", ".py")

# In .py files ONLY comment lines are eligible. A comment is prose and obeys the
# same rules as markdown; a code line may contain a string literal that IS a path
# and has no English grammar around it to judge by. That distinction is the whole
# lesson of the first attempt, encoded.
PY_COMMENT = re.compile(r"^\s*#")

# Files whose SUBJECT is paths. Their correct content looks exactly like the
# defect -- mapping tables, known-directory lists, worked examples of the
# mangle. Includes this script and its detector, which rewrote their own
# docstrings and calibration inputs on the first run.
SKIP_FILES = {
    "fix_reorg_mangles.py", "detect_reorg_mangles.py",
    "fix_mangled_identifiers.py", "reorg_reader.py", "reorg_2026_08_07.py",
    "check_broken_pointers.py", "anchor_repo_root.py", "repoint-paths-safely",
    "validate_doc_pointers.py", "check_brenton_source_parity.py",
}


def fix_line(line: str):
    """Return (new_line, n_fixed). Conservative by construction."""
    out, last, n = [], 0, 0
    for m in PAT.finditer(line):
        before = line[:m.start()]
        # inside backticks?
        if before.count("`") % 2 == 1:
            continue
        # markdown link target?
        if re.search(r"\]\([^)]*$", before):
            continue
        # locative preposition immediately before -> a real directory reference
        if GUARD.search(before):
            continue
        out.append(line[last:m.start()])
        out.append(m.group(2))
        last = m.end()
        n += 1
    out.append(line[last:])
    return "".join(out), n


def calibrate() -> bool:
    ok = True
    cases = [
        ("defensible against the 1-method/canon.", "defensible against the canon.", 1,
         "bare noun restored"),
        ("producer 5-machinery/validators don't match",
         "producer validators don't match", 1, "bare plural restored"),
        (r'r"BC|test|5-machinery/tests|second"', r'r"BC|test|tests|second"', 1,
         "regex alternation restored"),
        ("the scripts live in 5-machinery/scripts",
         "the scripts live in 5-machinery/scripts", 0,
         "locative preposition GUARDS a real reference"),
        ("see `5-machinery/scripts` for detail",
         "see `5-machinery/scripts` for detail", 0, "backticked path untouched"),
        ("[link](5-machinery/scripts)", "[link](5-machinery/scripts)", 0,
         "markdown link target untouched"),
        ("run 5-machinery/scripts/build_log.py now",
         "run 5-machinery/scripts/build_log.py now", 0, "deeper path untouched"),
        ("plain prose about canon", "plain prose about canon", 0,
         "unprefixed noun untouched"),
        ("edit 1-method/canon.md today", "edit 1-method/canon.md today", 0,
         "a real .md filename is NOT stripped"),
        ("per the 1-method/canon, yes", "per the canon, yes", 1,
         "comma after the noun does not hide it"),
    ]
    for src, want, want_n, why in cases:
        got, n = fix_line(src)
        hit = got == want and n == want_n
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why}", file=sys.stderr)
        if not hit:
            print(f"        got {got!r} n={n}", file=sys.stderr)
    return ok


def run(repo: str, dry: bool):
    root = os.path.join(REPOS, repo)
    files_changed = total = 0
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in files:
            if not fn.endswith(EXTS) or fn in SKIP_FILES:
                continue
            full = os.path.join(dirpath, fn)
            try:
                text = open(full, encoding="utf-8").read()
            except (OSError, UnicodeDecodeError):
                continue
            lines = text.splitlines(keepends=True)
            new, n_file, in_fence = [], 0, False
            for line in lines:
                body = line.rstrip("\r\n")
                tail = line[len(body):]
                # A fenced block is code or a worked example. Both are contexts
                # where the prefix may be correct and prose rules do not apply.
                if body.lstrip().startswith("```"):
                    in_fence = not in_fence
                    new.append(line)
                    continue
                if in_fence or (fn.endswith(".md") and body.startswith("    ")):
                    new.append(line)
                    continue
                # Python: comment lines only. Never a code line.
                if fn.endswith(".py") and not PY_COMMENT.match(body):
                    new.append(line)
                    continue
                fixed, n = fix_line(body)
                new.append(fixed + tail)
                n_file += n
            if n_file:
                files_changed += 1
                total += n_file
                if not dry:
                    open(full, "w", encoding="utf-8", newline="").write("".join(new))
    return files_changed, total


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repos", nargs="*")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--calibrate", action="store_true")
    args = ap.parse_args()

    if args.calibrate:
        print("calibration -- restore nouns, never touch a real path", file=sys.stderr)
        ok = calibrate()
        print("\nCALIBRATED" if ok else "\nMISCALIBRATED", file=sys.stderr)
        return 0 if ok else 1

    if not calibrate():
        print("MISCALIBRATED -- refusing to rewrite", file=sys.stderr)
        return 1
    print()
    targets = args.repos or [d for d in sorted(os.listdir(REPOS))
                             if os.path.isdir(os.path.join(REPOS, d, ".git"))]
    grand_f = grand_n = 0
    for repo in targets:
        f, n = run(repo, args.check)
        grand_f += f
        grand_n += n
        verb = "would fix" if args.check else "fixed"
        print(f"    {repo:20} {verb} {n:>4} in {f:>3} file(s)")
    print(f"\n    TOTAL {'would fix' if args.check else 'fixed'}: {grand_n} in {grand_f} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
