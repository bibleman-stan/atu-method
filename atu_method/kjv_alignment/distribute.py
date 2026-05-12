"""Per-verse KJV-to-ATU-line distribution algorithm.

Input
-----
- source_tokens_per_line: list[list[SourceToken]] — the source-language
  ATU lines for the verse, each line being a list of source tokens (already
  segmented by the consuming repo's parser). Each SourceToken carries a
  list of normalised Strong's numbers and its surface text.
- kjv_words: list[KjvWord] — the KJV verbatim words for this verse, in KJV
  reading order, with per-word Strong's tagging (from MetaV).

Output
------
- list[str] — one English string per input ATU line, KJV verbatim, in KJV
  verse-position order within each line. Translator-supplied (no-Strong's)
  KJV words attach to the line of their nearest claimed neighbour.

Algorithm
---------
1. Source-token loop in textual order. For each source token, find the
   next UNCLAIMED KJV word whose Strong's set shares any base number with
   the source token's Strong's set. Mark that KJV word with the line index
   the source token belongs to. (First-match-wins on the KJV side, walking
   in KJV vpos order. Source tokens without Strong's claim nothing.)

   When a source-token Strong's set is exhausted but other KJV words still
   match its Strong's later, we ALSO claim those subsequent matches for the
   same line (KJV often translates one source word into multiple English
   words — e.g. Greek aorist ἕξει -> "shall be with child"). We achieve
   this by, after the primary first-match-wins pass, sweeping any still-
   unclaimed KJV word whose ONLY-Strong's matches a source token already
   placed on a line, and attaching it to the same line.

2. Translator-supplied KJV words (empty Strong's): attach to the line of
   the NEAREST non-empty-Strong's neighbour. Preference: next non-italic
   word (forward look). Fallback: previous non-italic word. If both
   directions are empty (entire verse unclaimed), every KJV word goes to
   line 0.

3. Render: for each line, sort its assigned KJV words by vpos and join.
   Lines with no assignments render as the empty string (caller decides
   whether to fall back to "—" / placeholder / etc.).

Correctness invariants
----------------------
- Sum of KJV-word-count per output line == total KJV-word-count in input.
  (No words lost. No words duplicated.)
- Each output line's KJV words are in KJV verse-position order.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from atu_method.kjv_alignment.metav_loader import KjvWord


@dataclass(frozen=True)
class SourceToken:
    """One source-language token in textual order.

    Attributes:
        text: surface form (Greek / Hebrew)
        strongs_list: normalised base Strong's numbers (may be empty)
    """

    text: str
    strongs_list: tuple[str, ...] = field(default_factory=tuple)


def _strongs_overlap(a: tuple[str, ...], b: tuple[str, ...]) -> bool:
    """True if a and b share any Strong's base number."""
    if not a or not b:
        return False
    sb = set(b)
    return any(x in sb for x in a)


def distribute_kjv_to_atu_lines(
    source_tokens_per_line: list[list[SourceToken]],
    kjv_words: list[KjvWord],
) -> list[str]:
    """Distribute KJV words to source-language ATU lines.

    See module docstring for the full algorithm.

    Args:
        source_tokens_per_line: per-line lists of source tokens. Order
            within each line is irrelevant for distribution (we only use
            the line-index assignment), but cross-line order matters: the
            first token of line 0 is the first source token of the verse,
            and so on.
        kjv_words: KJV words for the verse, in KJV reading order
            (sorted by vpos).

    Returns:
        One English string per ATU line. Same length as
        source_tokens_per_line. Each string is KJV verbatim,
        KJV-vpos-ordered.
    """
    n_lines = len(source_tokens_per_line)
    if n_lines == 0:
        return []

    # Sort defensively by vpos
    kjv_sorted = sorted(kjv_words, key=lambda w: w.vpos)
    n_kjv = len(kjv_sorted)

    # vpos -> line index assignment (None if unassigned)
    assignment: list[int | None] = [None] * n_kjv
    # bool by KJV-index: claimed by primary pass (used to mark "anchored")
    claimed: list[bool] = [False] * n_kjv

    # Flatten source tokens to (line_idx, token) in textual order so we
    # walk the source-language pass in canonical order.
    flat_source: list[tuple[int, SourceToken]] = []
    for line_idx, tokens in enumerate(source_tokens_per_line):
        for tok in tokens:
            flat_source.append((line_idx, tok))

    # Pass A: primary first-match-wins on the KJV side.
    # For each source token (in textual order), find the next unclaimed KJV
    # word whose Strong's overlaps; claim it for this source token's line.
    # We also remember, per source token, what line it placed onto for the
    # subsequent "synonymy sweep."
    source_token_line: list[int] = []
    for line_idx, tok in flat_source:
        source_token_line.append(line_idx)
        if not tok.strongs_list:
            continue
        for i, kw in enumerate(kjv_sorted):
            if claimed[i]:
                continue
            if not kw.strongs_list:
                continue
            if _strongs_overlap(tok.strongs_list, kw.strongs_list):
                claimed[i] = True
                assignment[i] = line_idx
                break

    # Pass B: synonymy sweep. Any KJV word still unclaimed whose Strong's
    # overlaps SOME source token in the verse should attach to the LAST
    # line whose source tokens carry an overlapping Strong's. This handles
    # one-source-token -> multiple-KJV-words (e.g. ἕξει -> "shall be with
    # child" where MetaV gives "with child" the same G1722/G1064/G2192 set
    # that the single Greek word carries).
    #
    # We pick the *last* matching source-line because KJV multi-word
    # renderings of a single source token typically stay together; the
    # source token's line is the natural home.
    for i, kw in enumerate(kjv_sorted):
        if claimed[i]:
            continue
        if not kw.strongs_list:
            continue
        match_line: int | None = None
        for line_idx, tok in flat_source:
            if _strongs_overlap(tok.strongs_list, kw.strongs_list):
                match_line = line_idx
        if match_line is not None:
            assignment[i] = match_line
            claimed[i] = True

    # Pass C: translator-supplied (no-Strong's) KJV words attach to the
    # nearest assigned-or-anchored neighbour. Preference: next forward in
    # vpos order. Fallback: previous backward. Implementation: simple two-
    # direction scan.
    for i, kw in enumerate(kjv_sorted):
        if assignment[i] is not None:
            continue
        # Forward look
        forward: int | None = None
        for j in range(i + 1, n_kjv):
            if assignment[j] is not None:
                forward = assignment[j]
                break
        # Backward look
        backward: int | None = None
        for j in range(i - 1, -1, -1):
            if assignment[j] is not None:
                backward = assignment[j]
                break
        if forward is not None:
            assignment[i] = forward
        elif backward is not None:
            assignment[i] = backward
        else:
            # Whole verse unclaimed (no source tokens matched anything).
            # Dump all KJV words on line 0 by default.
            assignment[i] = 0

    # Pass D: render. Group by line, preserve KJV vpos order.
    per_line: list[list[KjvWord]] = [[] for _ in range(n_lines)]
    for i, kw in enumerate(kjv_sorted):
        line = assignment[i]
        # Defensive clamp: if a line ref escapes due to caller weirdness,
        # park it on the last line rather than crashing.
        if line is None or line < 0 or line >= n_lines:
            line = max(0, n_lines - 1)
        per_line[line].append(kw)

    out: list[str] = []
    for words in per_line:
        words.sort(key=lambda w: w.vpos)
        parts: list[str] = []
        for w in words:
            parts.append(w.render())
        out.append(" ".join(parts).strip())
    return out
