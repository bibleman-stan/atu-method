"""
Map (sent_id, token_id) in a CoNLL-U file to v2-mine-style line numbers.

CoNLL-U sentences are parser-output-bounded (typically one per verse, but
sometimes spanning verses on long anacolutha). The "v2-mine" file format is
one ATU per line plus optional verse-number marker lines (e.g., `29:11`).
This mapping lets a UD-query validator violation report point back to the
exact source line a token sits on.

Algorithm: walk forward through v2-mine content tokens, advancing through
the CoNLL-U FORM stream in sync. When the FORM stream crosses a v2-mine
newline boundary, increment the line cursor.

Caveats:
- Assumes the v2-mine file state matches the parse state (no edits to the
  source text since the parser ran).
- A FORM that doesn't appear in the upcoming v2-mine slice gets skipped
  (with a warning if verbose). This shouldn't happen for a clean parse.

This module is the universal infrastructure piece. Per-corpus code that
needs to resolve `book_id -> (v2_path, conllu_path)` should provide its
own resolver and call `build_line_map`/`build_line_map_full` with the
resolved paths.

Usage:
    from atu_method.parsing.line_mapping import build_line_map

    m = build_line_map(
        v2_path=Path("data/text-files/v2-mine/04-enos-2020-sb-v2.txt"),
        conllu_path=Path("data/parses/llm-direct/enos.conllu"),
    )
    line_num = m[("0", 7)]  # the 'that' complementizer in sent 0
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from atu_method.parsing.conllu_query import load_conllu


VERSE_NUM_RE = re.compile(r"^\s*\d+:\d+\s*$")


def _v2_content_lines(v2_path: Path) -> list[tuple[int, str]]:
    """Return [(line_num, content), ...] for v2-mine content lines.
    Skips blank lines and verse-number marker lines (matching VERSE_NUM_RE).
    """
    out: list[tuple[int, str]] = []
    with open(v2_path, encoding="utf-8") as f:
        for ln, raw in enumerate(f, start=1):
            stripped = raw.rstrip()
            if not stripped.strip():
                continue
            if VERSE_NUM_RE.match(stripped):
                continue
            out.append((ln, stripped))
    return out


def build_line_map_full(
    v2_path: Path,
    conllu_path: Path,
    *,
    verbose: bool = False,
) -> dict[tuple[str, int], tuple[int, int]]:
    """Return {(sent_id, token_id): (v2_line_num, col_offset)} for every
    parsed token.

    `col_offset` is the character offset of the token's first character
    *within* its v2-mine line. Appliers can use this to know exactly where
    to insert a line break (split before col_offset -> ATU break exactly
    before the token).

    Tokens that cannot be aligned are omitted; warning to stderr if verbose.
    """
    content = _v2_content_lines(v2_path)

    # Build a flat character stream with line-start offsets recorded.
    full_text_parts: list[str] = []
    line_starts: list[tuple[int, int]] = []  # (v2_line_num, char_offset_in_full_text)
    cursor = 0
    for line_num, text in content:
        line_starts.append((line_num, cursor))
        full_text_parts.append(text)
        full_text_parts.append(" ")
        cursor += len(text) + 1
    full_text = "".join(full_text_parts)

    import bisect
    line_offsets = [c for _, c in line_starts]

    def line_and_col(idx: int) -> tuple[int, int]:
        """Return (v2_line_num, col_offset_within_line) for char position idx."""
        i = bisect.bisect_right(line_offsets, idx) - 1
        if i < 0:
            i = 0
        line_num, line_start_offset = line_starts[i]
        col_offset = idx - line_start_offset
        return (line_num, col_offset)

    sentences = load_conllu(conllu_path)

    pos = 0
    prev_anchor = 0
    out: dict[tuple[str, int], tuple[int, int]] = {}
    misses = 0
    anchor_misses = 0

    def normalize(s: str) -> str:
        return " ".join(s.split())

    for sent in sentences:
        sent_text_norm = normalize(sent.text)
        if sent_text_norm:
            anchor_key = sent_text_norm[:60] if len(sent_text_norm) >= 60 else sent_text_norm
            anchor_idx = full_text.find(anchor_key, prev_anchor)
            if anchor_idx < 0:
                anchor_idx = full_text.find(anchor_key)
            if anchor_idx >= 0:
                pos = anchor_idx
                prev_anchor = anchor_idx + 1
            else:
                anchor_misses += 1
                if verbose:
                    print(f"[anchor-miss] sent={sent.sent_id}: {anchor_key!r} not found",
                          file=sys.stderr)

        for tok in sent.tokens:
            form = tok.form
            idx = full_text.find(form, pos)
            if idx == -1:
                misses += 1
                if verbose:
                    print(f"[miss] sent={sent.sent_id} tok={tok.id} form={form!r}",
                          file=sys.stderr)
                continue
            out[(sent.sent_id, tok.id)] = line_and_col(idx)
            pos = idx + len(form)

    if (misses or anchor_misses) and verbose:
        total = sum(len(s.tokens) for s in sentences)
        print(f"[line_mapping] {misses} token misses, {anchor_misses} sentence-anchor misses "
              f"(of {total} tokens, {len(sentences)} sentences)", file=sys.stderr)

    return out


def build_line_map(
    v2_path: Path,
    conllu_path: Path,
    *,
    verbose: bool = False,
) -> dict[tuple[str, int], int]:
    """Backward-compat wrapper: return {(sent_id, token_id): v2_line_num}.

    For new appliers that need char-offset precision, use
    build_line_map_full() instead.
    """
    full = build_line_map_full(v2_path, conllu_path, verbose=verbose)
    return {key: line_col[0] for key, line_col in full.items()}
