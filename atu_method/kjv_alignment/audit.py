"""Corpus-wide audit of generated KJV eng-gloss outputs.

Detects symptoms of distribute()-class bugs by comparing the per-cola
output against the canonical KJV verse text from MetaV. Five checks:

  1. cross-line word duplication: a non-italic KJV word appears in TWO
     ATU-line outputs for the same verse when the KJV verse text contains
     it only once. (The Gen 1:2 "upon" smoking-gun.)
  2. cross-line word loss: a non-italic KJV word appears in the KJV verse
     text but in ZERO ATU-line outputs.
  3. trailing/leading italic orphans: line starts or ends with a
     translator-supplied (no-Strong's) KJV word that has NO Strong's-tagged
     KJV neighbour on the same line whose vpos brackets the orphan.
  4. word-order inversion within a line: a KJV word appearing earlier in
     a line's output than another that comes before it in KJV verse order.
  5. empty ATU lines (em-dash placeholders): each empty/placeholder line.

Output: text report to stdout, plus an optional JSON dump for downstream
machinery. Tracks per-corpus, per-check counts and per-verse top-10
worst offenders.

CLI
---
  python -m atu_method.kjv_alignment.audit \
    --eng-gloss-dir <path> \
    --metav-dir <path> \
    --book-osis-map "Genesis=Gen,Exodus=Exod,..."

Usage from each corpus's repo: run with the eng-gloss directory of that
repo plus the central METAV_DIR. Provides a single number per check
plus per-verse details for the worst offenders.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

from atu_method.kjv_alignment.metav_loader import (
    OSIS_TO_BOOK_ID,
    KjvWord,
    load_kjv_strongs_index,
)

VERSE_REF_RE = re.compile(r"^\d+:\d+$")
WORD_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")
EMPTY_PLACEHOLDERS = {"—", "--", ""}


def _normalize_word(w: str) -> str:
    """Case-insensitive comparable form for KJV-word matching."""
    return w.strip("'\".,;:!?()[]{}—–-").lower()


def _extract_kjv_words(line: str) -> list[str]:
    """Pull comparable word-tokens from a rendered KJV line."""
    out: list[str] = []
    for m in WORD_TOKEN_RE.findall(line):
        norm = _normalize_word(m)
        if norm:
            out.append(norm)
    return out


def _parse_eng_gloss_chapter(path: Path) -> list[tuple[str, list[str]]]:
    """Parse a `<book>-NN.txt` eng-gloss file.

    Returns: list of (verse_ref, [line, line, ...]). Verses end at the
    next verse-ref or EOF — NOT at the first blank line. Blanks inside
    a verse are legitimate empty content slots (when a grk ATU line
    receives no KJV mapping). Trailing blanks at verse-close are
    stripped (they're the verse-separator).
    """
    verses: list[tuple[str, list[str]]] = []
    current_ref: str | None = None
    current_lines: list[str] = []

    def _close():
        nonlocal current_ref, current_lines
        if current_ref is not None:
            # Strip trailing separator blanks
            while current_lines and current_lines[-1].strip() == "":
                current_lines.pop()
            if current_lines:
                verses.append((current_ref, current_lines))
        current_ref = None
        current_lines = []

    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\r\n")
            if VERSE_REF_RE.match(line.strip()):
                _close()
                current_ref = line.strip()
                continue
            if current_ref is not None:
                current_lines.append(line)
    _close()
    return verses


def _verse_kjv_words(metav_verse: list[KjvWord]) -> list[tuple[str, bool, int]]:
    """Return [(normalized_text, is_strongs_tagged, vpos), ...] in vpos order."""
    out = []
    for w in sorted(metav_verse, key=lambda x: x.vpos):
        norm = _normalize_word(w.text)
        if not norm:
            continue
        is_tagged = len(w.strongs_list) > 0
        out.append((norm, is_tagged, w.vpos))
    return out


def audit_verse(
    verse_ref: str,
    cola_lines: list[str],
    metav_verse: list[KjvWord],
    book_label: str,
    prior_verse_last_line: str | None = None,
) -> dict:
    """Audit one verse's cola distribution against MetaV truth.

    Args:
        verse_ref: "ch:vs" form (e.g. "3:2").
        cola_lines: list of rendered KJV English lines for this verse.
        metav_verse: MetaV KJV words for this verse, in vpos order.
        book_label: OSIS book code (e.g. "Matt").
        prior_verse_last_line: the last KJV English line of the IMMEDIATELY
            PRECEDING verse, if any. Used to filter §5.1-fold artifacts
            from the loss count — when v4-editorial has a cross-verse
            marker on the prior verse's last line, KJV words from the
            current verse's TAGNT-canonical start appear there instead
            of on the current verse's output, producing apparent "loss"
            flags that are actually correct cross-verse fold behavior.

    Returns a dict of findings keyed by check name.
    """
    findings: dict[str, list[dict]] = defaultdict(list)
    prior_last_words = set(_extract_kjv_words(prior_verse_last_line)) if prior_verse_last_line else set()
    kjv_seq = _verse_kjv_words(metav_verse)
    kjv_count = defaultdict(int)
    for norm, _, _ in kjv_seq:
        kjv_count[norm] += 1
    # Map word -> list of vpos (in vpos order) so we can validate ordering
    vpos_lookup: dict[str, list[int]] = defaultdict(list)
    is_tagged_lookup: dict[str, list[bool]] = defaultdict(list)
    # Per-vpos tag lookup: vpos -> is_tagged. The orphan_line check needs
    # the SPECIFIC occurrence's tag status, not the FIRST occurrence's.
    # E.g., 1Pet 4:4 has "of" twice — vpos 15 (italic) + vpos 19 (G987 for
    # βλασφημοῦντες) — and is_tagged_lookup["of"][0]=False would
    # wrongly mark line 3 as orphan when its "of" is the tagged vpos-19 one.
    vpos_to_tagged: dict[int, bool] = {}
    for norm, is_tagged, vpos in kjv_seq:
        vpos_lookup[norm].append(vpos)
        is_tagged_lookup[norm].append(is_tagged)
        vpos_to_tagged[vpos] = is_tagged

    # Tally output occurrences per word + assign each occurrence a vpos
    # (consume in vpos order from vpos_lookup as we walk the cola lines).
    out_count = defaultdict(int)
    per_line_words: list[list[tuple[str, int | None]]] = []
    vpos_iter: dict[str, list[int]] = {k: list(v) for k, v in vpos_lookup.items()}

    for cola in cola_lines:
        words: list[tuple[str, int | None]] = []
        for w in _extract_kjv_words(cola):
            out_count[w] += 1
            assigned_vpos: int | None = None
            if vpos_iter.get(w):
                assigned_vpos = vpos_iter[w].pop(0)
            words.append((w, assigned_vpos))
        per_line_words.append(words)

    # Check 1: cross-line word duplication
    # Two sub-checks:
    #  (a) Total output count of word w exceeds KJV verse count.
    #  (b) Per-line count of word w exceeds KJV count overall (same-line
    #      dupes like Gen 1:2 "upon ... upon" on one cola).
    word_to_lines: dict[str, list[int]] = defaultdict(list)
    for li, words in enumerate(per_line_words):
        for w, _ in words:
            word_to_lines[w].append(li)
    for w, lines in word_to_lines.items():
        if not w:
            continue
        out_total = len(lines)
        kjv_n = kjv_count.get(w, 0)
        # Sub-check (a): cross-verse over-count
        if out_total > kjv_n and kjv_n > 0:
            findings["duplication"].append({
                "book": book_label, "ref": verse_ref, "word": w,
                "kjv_count": kjv_n, "out_count": out_total,
                "out_lines": sorted(set(lines)),
                "kind": "over-emitted",
            })
            continue  # don't double-flag
        # Sub-check (b): per-line concentration (a single line has more
        # of this word than the entire KJV verse contains)
        per_line_counts = defaultdict(int)
        for li in lines:
            per_line_counts[li] += 1
        max_on_line = max(per_line_counts.values()) if per_line_counts else 0
        if kjv_n > 0 and max_on_line > kjv_n:
            findings["duplication"].append({
                "book": book_label, "ref": verse_ref, "word": w,
                "kjv_count": kjv_n, "out_count": out_total,
                "max_on_line": max_on_line,
                "out_lines": sorted(set(lines)),
                "kind": "per-line-concentration",
            })

    # Check 2: cross-line word loss — KJV word in verse but in fewer output
    # lines than KJV count. Note: BHS-vs-KJV verse-number shifts in Psalms,
    # 1Sam-Kgs, Romans etc. produce massive false positives for this check
    # because the comparison key is BHS-numbered while MetaV is KJV-numbered.
    # We only flag when out_count is STRICTLY less than kjv_count AND there's
    # at least SOME output (a totally empty verse is the BHS-shift signature
    # and we skip those).
    total_out_words = sum(len(words) for words in per_line_words)
    if total_out_words > 0:
        for w, n in kjv_count.items():
            if n > 0 and out_count.get(w, 0) < n:
                tagged_anywhere = any(is_tagged_lookup.get(w, [False]))
                # §5.1 cross-verse-fold filter: when v4-editorial places a
                # superscript marker on the prior verse's last line, KJV
                # words from THIS verse's TAGNT-canonical start get
                # rendered on the prior verse's last line instead. The
                # audit's per-verse loss check can't distinguish that
                # from a real bug. Heuristic: if the lost word appears in
                # the prior verse's last line, classify as a fold artifact
                # — separate bucket, NOT counted in main loss.
                if w in prior_last_words:
                    findings["loss_fold_artifact"].append({
                        "book": book_label, "ref": verse_ref, "word": w,
                        "kjv_count": n, "out_count": out_count.get(w, 0),
                        "strongs_tagged": tagged_anywhere,
                    })
                else:
                    findings["loss"].append({
                        "book": book_label, "ref": verse_ref, "word": w,
                        "kjv_count": n, "out_count": out_count.get(w, 0),
                        "strongs_tagged": tagged_anywhere,
                    })

    # Check 3: trailing/leading italic orphans
    # Flag a line as orphan when NONE of its words map to a Strong's-tagged
    # vpos in MetaV. Per-vpos tag lookup (not per-word) — a repeated word
    # may be italic at one vpos and Strong's-tagged at another.
    for li, words in enumerate(per_line_words):
        if not words:
            continue
        tagged_on_line = [
            v for (_, v) in words
            if v is not None and vpos_to_tagged.get(v, False)
        ]
        if not tagged_on_line:
            findings["orphan_line"].append({
                "book": book_label, "ref": verse_ref,
                "line_idx": li, "snippet": cola_lines[li][:80],
            })

    # Build per-line Strong's sets for the inherent/actionable discriminator
    # used in the cross-line and within-line monotonicity checks below.
    # A flagged vpos is "actionable" (likely a real algorithm bug — the
    # algorithm could have placed it differently) when the same Strong's
    # has matched output on more than one line. It's "inherent" (no fix
    # possible at this layer — the line break forces it) when only the
    # claiming line has output for that Strong's.
    per_line_strongs: list[set[str]] = []
    metav_by_vpos = {w.vpos: w for w in metav_verse}
    for words in per_line_words:
        line_strongs: set[str] = set()
        for _w, v in words:
            if v is None:
                continue
            kw = metav_by_vpos.get(v)
            if kw is not None:
                for s in kw.strongs_list:
                    line_strongs.add(s)
        per_line_strongs.append(line_strongs)

    def _classify_flag(flagged_line: int, flagged_vpos: int) -> str:
        """Return 'inherent', 'actionable', or 'italic'."""
        kw = metav_by_vpos.get(flagged_vpos)
        if kw is None:
            return "unknown"
        if not kw.strongs_list:
            return "italic"
        for li, s_set in enumerate(per_line_strongs):
            if li == flagged_line:
                continue
            if any(s in s_set for s in kw.strongs_list):
                return "actionable"
        return "inherent"

    # Check 4a: cross-line monotonicity. Line N's max vpos should be <
    # line N+1's min vpos. Violations are the Gen-1:2 class (a later line
    # has a word with vpos earlier than the previous line's words).
    line_vpos_ranges: list[tuple[int | None, int | None]] = []
    for words in per_line_words:
        vps = [v for (_, v) in words if v is not None]
        if vps:
            line_vpos_ranges.append((min(vps), max(vps)))
        else:
            line_vpos_ranges.append((None, None))
    for li in range(len(line_vpos_ranges) - 1):
        cur_max = line_vpos_ranges[li][1]
        nxt_min = line_vpos_ranges[li + 1][0]
        if cur_max is not None and nxt_min is not None and nxt_min < cur_max:
            # Find which word actually inverts.
            for (w, vpos) in per_line_words[li]:
                if vpos is not None and vpos > nxt_min:
                    cls = _classify_flag(li, vpos)
                    bucket = "duplication" if cls == "actionable" else "duplication_inherent"
                    findings[bucket].append({
                        "book": book_label, "ref": verse_ref,
                        "kind": "cross-line-inversion",
                        "classification": cls,
                        "word": w, "line_idx": li,
                        "vpos": vpos, "next_line_min_vpos": nxt_min,
                    })
                    break

    # Check 4: word-order inversion within a line
    for li, words in enumerate(per_line_words):
        prev_vpos: int | None = None
        for w, vpos in words:
            if vpos is None:
                continue
            if prev_vpos is not None and vpos < prev_vpos:
                cls = _classify_flag(li, vpos)
                bucket = "order_inversion" if cls == "actionable" else "order_inversion_inherent"
                findings[bucket].append({
                    "book": book_label, "ref": verse_ref, "line_idx": li,
                    "classification": cls,
                    "word": w, "vpos": vpos, "prev_vpos": prev_vpos,
                })
            if prev_vpos is None or vpos > prev_vpos:
                prev_vpos = vpos

    # Check 5: empty / em-dash placeholder lines
    for li, cola in enumerate(cola_lines):
        stripped = cola.strip()
        if stripped in EMPTY_PLACEHOLDERS:
            findings["empty_line"].append({
                "book": book_label, "ref": verse_ref, "line_idx": li,
            })

    return findings


def audit_book_dir(
    book_dir: Path,
    metav_index,
    book_osis: str,
) -> dict:
    """Audit one book directory of <book>-NN.txt eng-gloss files."""
    book_id = OSIS_TO_BOOK_ID.get(book_osis)
    if book_id is None:
        return {"error": f"unknown OSIS code: {book_osis}"}

    findings: dict[str, list[dict]] = defaultdict(list)
    chapter_files = sorted(book_dir.glob("*.txt"))
    for cf in chapter_files:
        m = re.search(r"-(\d+)\.txt$", cf.name)
        if not m:
            continue
        chapter = int(m.group(1))
        verses = _parse_eng_gloss_chapter(cf)
        prior_last_line: str | None = None
        for ref, cola_lines in verses:
            try:
                ch_str, vs_str = ref.split(":")
                ch = int(ch_str)
                vs = int(vs_str)
            except ValueError:
                prior_last_line = cola_lines[-1] if cola_lines else None
                continue
            metav_key = (book_id, ch, vs)
            metav_verse = metav_index.get(metav_key)
            if metav_verse is None:
                prior_last_line = cola_lines[-1] if cola_lines else None
                continue
            verse_findings = audit_verse(
                ref, cola_lines, metav_verse, book_label=book_osis,
                prior_verse_last_line=prior_last_line,
            )
            for k, v in verse_findings.items():
                findings[k].extend(v)
            prior_last_line = cola_lines[-1] if cola_lines else None
    return findings


def audit_corpus(
    eng_gloss_root: Path,
    metav_dir: Path,
    book_osis_map: dict[str, str],
) -> dict:
    """Audit a full corpus tree (one subdir per book).

    Args:
        eng_gloss_root: e.g. readers-tanakh/data/text-files/v2/eng-gloss/
        metav_dir: MetaV CSV directory
        book_osis_map: {subdir_name -> OSIS_book_code}
    """
    print(f"Loading MetaV index from {metav_dir}...", file=sys.stderr)
    metav_index = load_kjv_strongs_index(metav_dir)

    all_findings: dict[str, list[dict]] = defaultdict(list)
    book_subdirs = sorted(p for p in eng_gloss_root.iterdir() if p.is_dir())
    for bd in book_subdirs:
        osis = book_osis_map.get(bd.name)
        if osis is None:
            print(f"  SKIP {bd.name} (no OSIS map)", file=sys.stderr)
            continue
        print(f"  auditing {bd.name} ({osis})...", file=sys.stderr)
        book_findings = audit_book_dir(bd, metav_index, osis)
        for k, v in book_findings.items():
            if isinstance(v, list):
                all_findings[k].extend(v)

    return all_findings


def print_report(findings: dict, top_n: int = 10) -> None:
    """Print a human-readable summary + top-N offenders per check."""
    checks = [
        "duplication", "duplication_inherent",
        "loss", "loss_fold_artifact",
        "orphan_line",
        "order_inversion", "order_inversion_inherent",
        "empty_line",
    ]
    print("=" * 70)
    print("KJV-DISTRIBUTION AUDIT SUMMARY")
    print("=" * 70)
    for check in checks:
        items = findings.get(check, [])
        print(f"\n{check}: {len(items)} flag(s)")
        if items:
            # Top-N by frequency of book/ref OR just first N
            for item in items[:top_n]:
                print(f"  {item}")
    print("=" * 70)


# Convenient default OSIS maps for the two consumers
TANAKH_BOOK_MAP = {
    "01-genesis": "Gen", "02-exodus": "Exod", "03-leviticus": "Lev",
    "04-numbers": "Num", "05-deuteronomy": "Deut",
    "06-joshua": "Josh", "07-judges": "Judg", "08-ruth": "Ruth",
    "09-1samuel": "1Sam", "10-2samuel": "2Sam",
    "11-1kings": "1Kgs", "12-2kings": "2Kgs",
    "13-1chronicles": "1Chr", "14-2chronicles": "2Chr",
    "15-ezra": "Ezra", "16-nehemiah": "Neh", "17-esther": "Esth",
    "18-job": "Job", "19-psalms": "Ps", "20-proverbs": "Prov",
    "21-ecclesiastes": "Eccl", "22-songofsongs": "Song",
    "23-isaiah": "Isa", "24-jeremiah": "Jer", "25-lamentations": "Lam",
    "26-ezekiel": "Ezek", "27-daniel": "Dan",
    "28-hosea": "Hos", "29-joel": "Joel", "30-amos": "Amos",
    "31-obadiah": "Obad", "32-jonah": "Jonah",
    "33-micah": "Mic", "34-nahum": "Nah", "35-habakkuk": "Hab",
    "36-zephaniah": "Zeph", "37-haggai": "Hag", "38-zechariah": "Zech",
    "39-malachi": "Mal",
}

GNT_BOOK_MAP = {
    "01-matt": "Matt", "02-mark": "Mark", "03-luke": "Luke", "04-john": "John",
    "05-acts": "Acts", "06-rom": "Rom", "07-1cor": "1Cor", "08-2cor": "2Cor",
    "09-gal": "Gal", "10-eph": "Eph", "11-phil": "Phil", "12-col": "Col",
    "13-1thess": "1Thess", "14-2thess": "2Thess",
    "15-1tim": "1Tim", "16-2tim": "2Tim",
    "17-titus": "Titus", "18-phlm": "Phlm",
    "19-heb": "Heb", "20-jas": "Jas",
    "21-1pet": "1Pet", "22-2pet": "2Pet",
    "23-1john": "1John", "24-2john": "2John", "25-3john": "3John",
    "26-jude": "Jude", "27-rev": "Rev",
}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--eng-gloss-dir", required=True, type=Path,
                   help="root of <book-subdir>/<chapter>.txt eng-gloss files")
    p.add_argument("--metav-dir", required=True, type=Path,
                   help="MetaV CSV dir (atu-method/data/kjv-strongs)")
    p.add_argument("--corpus", choices=("tanakh", "gnt"), required=True,
                   help="which built-in book map to use")
    p.add_argument("--top", type=int, default=10,
                   help="top-N offenders per check (default 10)")
    p.add_argument("--json-out", type=Path, default=None,
                   help="optional JSON dump of all findings")
    args = p.parse_args(argv)

    book_map = TANAKH_BOOK_MAP if args.corpus == "tanakh" else GNT_BOOK_MAP
    findings = audit_corpus(args.eng_gloss_dir, args.metav_dir, book_map)
    print_report(findings, top_n=args.top)
    if args.json_out:
        args.json_out.write_text(
            json.dumps(findings, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"\nJSON dump: {args.json_out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
