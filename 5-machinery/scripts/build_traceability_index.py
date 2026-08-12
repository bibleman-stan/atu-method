#!/usr/bin/env python3
"""Emit the theory -> rule -> validator traceability table for Tanakh.

WHY THIS EXISTS. On 2026-08-11 the question was asked whether the rules are
grounded in scholarship or are a self-licking ice cream cone. The answer for
Tanakh turned out to be better than feared and worse than it looks:

  constraint_catalog_v1.md  26 entries, 26 with a **Source** line,
                            Joüon x32, Waltke-O'Connor x20 -- 100% cited
  binding-rules-hebrew.md   14 entries, 0 Source lines, 0 grammar citations

The catalog was moved to _archive/2026-05-18-mechanical-first-rewrite/ by commit
922001bc0, whose message calls it "superseded". The successor covers different
ground and carries none of the scholarly apparatus. Meanwhile the LIVE validator
names are catalog constraint names -- validate_construct_chain,
validate_verb_object_bond, validate_bonded_pair -- so the running code still
implements the archived, cited catalog while the live docs point at a master
index that is not there.

So the grounding is not missing. It is orphaned. This table is what makes that
visible per-rule instead of per-argument, and a blank cell is the point: an
empty Validator or Source column is a defect you can see.

WHAT THIS DOES NOT DO. It cannot tell whether a citation SUPPORTS its rule.
Joüon §129 establishes that construct chains are a recognised nominal unit; it
does not say never to break one across a colometric line. That inference is
ours. The Grounding column exists to keep that distinction visible, and only a
human can fill it honestly -- so the generator emits UNVERIFIED and refuses to
guess.

    python build_traceability_index.py --calibrate
    python build_traceability_index.py > ../2-evidence/traceability-tanakh.md
"""

import argparse
import json
import os
import re
import sys

REPOS = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
CATALOG = os.path.join(REPOS, "readers-tanakh", "1-method", "canon",
                       "constraint_catalog_v1.md")
VAL_DIR = os.path.join(REPOS, "readers-tanakh", "5-machinery", "validators")
# Human judgments live in a sidecar so the table stays regenerable. Hand-editing
# the emitted markdown would lose the curation on the next run -- the same shape
# of failure as every hand-maintained pointer this project has already lost.
GROUNDING = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))),
    "2-evidence", "traceability-grounding.json")

# Deliberately permissive. The first version required a section number after the
# prefix (JM\d+) and silently dropped three entries: JM-oath-formula,
# JM-cross-verse-continuity, JM-wayehi-fef-protasis. Those are the MOST
# interesting rows, not the least -- a JM prefix with no Joüon section is
# exactly the shape of a constraint that looks cited and is not. One of the
# three cites only our own canon.
ENTRY = re.compile(r"^### ((?:JM|SJ|M|H)\d*[a-z]?-[a-z0-9-]+)", re.M)
SOURCE = re.compile(r"^\s*-?\s*\*\*Source\*\*:\s*(.+)$", re.M)

# Tokens too generic to carry a match on their own. Without this, "clause"
# alone pairs almost anything with almost anything.
STOP = {"clause", "line", "bond", "integrity", "default", "group", "pair",
        "object", "split", "chain", "head", "policy", "handling", "formula"}


def slug_tokens(slug: str) -> set:
    return {t for t in slug.split("-") if t not in STOP and len(t) > 2}


def load_catalog():
    """Return [(constraint_id, source_text)] in document order."""
    text = open(CATALOG, encoding="utf-8").read()
    out, positions = [], [(m.group(1), m.start()) for m in ENTRY.finditer(text)]
    for i, (cid, pos) in enumerate(positions):
        end = positions[i + 1][1] if i + 1 < len(positions) else len(text)
        body = text[pos:end]
        m = SOURCE.search(body)
        out.append((cid, m.group(1).strip() if m else ""))
    return out


def load_validators():
    names = []
    for root, _, files in os.walk(VAL_DIR):
        if "__pycache__" in root:
            continue
        for f in files:
            if f.startswith(("validate_", "check_")) and f.endswith(".py"):
                names.append(f[:-3])
    return sorted(names)


def match(cid: str, validators: list) -> list:
    """Token-overlap match. Returns ALL candidates, not a best guess -- picking
    a winner between two plausible validators is exactly the judgment this
    script has no basis for making."""
    slug = cid.split("-", 1)[1]
    want = slug_tokens(slug)
    if not want:
        return []
    hits = []
    for v in validators:
        have = slug_tokens(v.replace("validate_", "").replace("check_", "").replace("_", "-"))
        if want & have:
            hits.append((len(want & have), v))
    hits.sort(reverse=True)
    top = [v for n, v in hits if n == hits[0][0]] if hits else []
    return top


def calibrate() -> bool:
    """Poles on the matcher. The known-bad cases matter more: a false pairing
    in this table would assert a rule is implemented when it is not."""
    ok = True
    vals = ["validate_construct_chain", "validate_bonded_pair",
            "validate_verb_object_bond", "validate_maqqef_group",
            "validate_short_orphan_line"]
    cases = [
        ("JM129-construct-chain", ["validate_construct_chain"], "exact concept matches"),
        ("JM177-bonded-pair", ["validate_bonded_pair"], "exact concept matches"),
        ("JM13-maqqef-group", ["validate_maqqef_group"], "stop-word 'group' does not block a real match"),
        ("JM999-nonexistent-thing", [], "unknown constraint yields NO match, not a guess"),
        ("JM998-line-split", [], "stop-words only -> refuses to match anything"),
    ]
    for cid, want, why in cases:
        got = match(cid, vals)
        hit = got == want
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why}  ({cid} -> {got or 'none'})", file=sys.stderr)
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibrate", action="store_true")
    args = ap.parse_args()

    if args.calibrate:
        print("calibration -- match real concepts, refuse to guess", file=sys.stderr)
        ok = calibrate()
        print("\nCALIBRATED" if ok else "\nMISCALIBRATED", file=sys.stderr)
        return 0 if ok else 1

    if not calibrate():
        print("MISCALIBRATED -- refusing to emit", file=sys.stderr)
        return 1

    cat = load_catalog()
    vals = load_validators()
    curated = {}
    if os.path.exists(GROUNDING):
        curated = json.load(open(GROUNDING, encoding="utf-8"))
    rows, unmatched_v = [], set(vals)
    for cid, src in cat:
        m = match(cid, vals)
        unmatched_v -= set(m)
        rows.append((cid, src, m))

    cited = sum(1 for _, s, _ in rows if s)
    linked = sum(1 for _, _, m in rows if m)

    print("# Traceability — Tanakh: theory → rule → validator\n")
    print("**Generated** by `5-machinery/scripts/build_traceability_index.py`. "
          "Regenerate rather than hand-edit the table; the Grounding column is "
          "the exception and is curated by hand.\n")
    print(f"- Constraints in catalog: **{len(rows)}**")
    print(f"- With a scholarly `Source`: **{cited}/{len(rows)}**")
    print(f"- With a name-matched validator: **{linked}/{len(rows)}**")
    print(f"- Validators with no matching constraint: **{len(unmatched_v)}**\n")
    print("> The catalog is at `readers-tanakh/_archive/2026-05-18-mechanical-first-rewrite/`.\n"
          "> It is **archived**, marked `Status: DRAFT`, and the six live files in\n"
          "> `1-method/canon/constraints/` still point to it as their master index.\n")
    print("## Grounding vocabulary\n")
    print("| Value | Means |")
    print("|---|---|")
    print("| `GROUNDED` | Source asserts the unit coheres **and** that this bears on segmentation |")
    print("| `DESCRIBED` | Source establishes the phenomenon; the segmentation inference is ours |")
    print("| `PROJECT` | No external source — a deliberate engineering decision |")
    print("| `UNGROUNDED` | Neither source nor rationale — candidate for retirement |")
    print("| `MISCITED` | The section named does not cover the claim. A defect in the **citation**, not a verdict on the rule. |")
    print("| `UNVERIFIED` | Not yet judged by a human. The generator never guesses. |\n")
    print("## Constraints\n")
    judged = sum(1 for cid, _, _ in rows if cid in curated)
    print(f"*Grounding judged: **{judged}/{len(rows)}**. Curated in "
          f"`2-evidence/traceability-grounding.json`, merged at build time so "
          f"regenerating never discards it.*\n")
    print("| Constraint | Source (scholarship) | Validator | Grounding |")
    print("|---|---|---|---|")
    for cid, src, m in rows:
        v = "<br>".join(f"`{x}`" for x in m) if m else "**— none —**"
        c = curated.get(cid)
        if c:
            g = f"`{c['grounding']}`"
            if c.get("checked"):
                g += f" ✓{c['checked']}"
            if c.get("note"):
                g += f" — {c['note']}"
        else:
            g = "`UNVERIFIED`"
        print(f"| [[{cid}]] | {src or '**— none —**'} | {v} | {g} |")

    # A judged row carrying the five protocol fields is a CHECKED citation; a
    # judged row without them is an opinion. The distinction is the whole point,
    # so print the receipts rather than leaving them in the sidecar.
    verified = [(cid, c) for cid, c in curated.items()
                if isinstance(c, dict) and c.get("quote")]
    if verified:
        print("\n## Verified against the source\n")
        print("Each entry below was judged only after opening the receipt. "
              "Quote is verbatim; page is as printed in the source, not the PDF page.\n")
        for cid, c in verified:
            print(f"### {cid} — `{c['grounding']}`\n")
            print(f"> {c['quote']}\n")
            print(f"- **Page**: {c.get('page','?')}")
            print(f"- **Edition**: {c.get('edition','— not recorded —')}")
            print(f"- **Receipt**: `{c.get('receipt','— none —')}`")
            print(f"- **Checked**: {c.get('checked','never')}\n")
            if c.get("assessment"):
                print(f"{c['assessment']}\n")

    if unmatched_v:
        print("\n## Validators with no matching constraint\n")
        print("Each is either implementing a rule absent from the catalog, or "
              "implementing nothing the catalog knows about. Both are defects.\n")
        for v in sorted(unmatched_v):
            print(f"- `{v}`")
    return 0


if __name__ == "__main__":
    sys.exit(main())
