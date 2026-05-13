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

Algorithm (Wave 7 — positional-aware monotonic matching)
--------------------------------------------------------
The Wave 5b algorithm walked source tokens in flat order and grabbed the
first KJV match per Strong's number. That works when source-line order
and KJV-vpos order march in lockstep, but breaks when (a) a source token's
Strong's appears earlier in KJV order than is positionally natural for its
line, or (b) source-token count > KJV count for some Strong's, so the
earlier source line steals a match that belongs positionally to a later
line. Gen 1:2's two Hebrew עַל preposition tokens (cola 2 and cola 3)
competing for KJV's single Strong's-tagged "upon" (vpos 23, in cola 3's
region) is the canonical instance — cola 2 stole vpos 23 and KJV's other
"upon" (vpos 11, translator-supplied) attached to cola 2 via forward-look,
duplicating the surface form "upon" onto cola 2.

The Wave 7 algorithm matches by Strong's number with two-stage logic:
1. Unambiguous Strong's (source-count <= kjv-count): monotonic 1:1.
   Establishes "anchor" KJV positions per line.
2. Over-supplied Strong's (source-count > kjv-count): each KJV occurrence
   goes to the source line whose existing anchors are positionally
   closest in KJV vpos. Falls back to monotonic if no anchors yet.

Pass B (synonymy sweep) and Pass C (italic attachment) become positional-
proximity-driven rather than first-source-token-wins. Pass C also respects
sentence-boundary punctuation (".", "!", "?") as a soft barrier when both
forward and backward neighbours exist.

Three passes total:

  A. Strong's matching (two sub-stages): claim KJV words whose Strong's
     overlap a source token. Within a Strong's class, k-th source token
     in flat order claims k-th KJV word in vpos order, EXCEPT when the
     source class is over-supplied — then each KJV match goes to the
     source line whose anchor claims are positionally nearest.

  B. Synonymy sweep: any KJV word still unclaimed whose Strong's overlap
     SOME source token's Strong's. Assign to the line whose anchors
     (now including A's claims) are positionally nearest.

  C. Translator-supplied (no-Strong's) KJV words: attach to the nearest
     non-italic neighbour. Forward preferred. If forward-vs-backward
     crosses a sentence boundary in one direction and not the other,
     prefer the un-crossed direction.

Strong's-tagged KJV words still unclaimed after A+B (no overlap found
anywhere in the verse) fall through to the positional-proximity sweep
(same logic as B but unconstrained by Strong's). The Wave 5b "park on
last line" defensive clamp is retired — positional proximity always wins.

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


_SENTENCE_PUNCT = {".", "!", "?"}


def _strongs_overlap(a: tuple[str, ...], b: tuple[str, ...]) -> bool:
    """True if a and b share any Strong's base number."""
    if not a or not b:
        return False
    sb = set(b)
    return any(x in sb for x in a)


def _line_nearest_anchor_distance(
    target_vpos: int,
    line_anchors: list[int],
) -> int:
    """Distance from target_vpos to nearest anchor on this line.

    Returns a large sentinel (10**9) when the line has no anchors yet — so
    a line with NO claims always loses to a line with at least one claim.
    """
    if not line_anchors:
        return 10**9
    return min(abs(target_vpos - a) for a in line_anchors)


def _pick_line_by_proximity(
    target_vpos: int,
    candidate_lines: list[int],
    per_line_anchors: list[list[int]],
    n_lines: int,
) -> int:
    """Pick the line in candidate_lines whose anchors are nearest to vpos.

    Ties broken by: prefer the line whose nearest anchor is AFTER (≥) the
    target vpos over a line whose nearest anchor is BEFORE (<). When both
    are forward or both backward, prefer the LATER line (higher line index)
    — KJV reading order flows forward; ambiguous adjacency more likely
    belongs to the line that owns the subsequent vposes. If all candidates
    have no anchors, return the first candidate.
    """
    def _score(line: int) -> tuple[int, int, int]:
        anchors = per_line_anchors[line]
        if not anchors:
            return (10**9, 0, line)
        # Distance to nearest anchor
        dist = min(abs(target_vpos - a) for a in anchors)
        # Direction-of-nearest: 0 if nearest anchor is ≥ target_vpos
        # (forward), 1 if < target_vpos (backward). Forward preferred.
        forward_anchors = [a for a in anchors if a >= target_vpos]
        nearest_is_forward = bool(forward_anchors) and (
            min(forward_anchors) - target_vpos == dist
        )
        return (dist, 0 if nearest_is_forward else 1, -line)

    return min(candidate_lines, key=_score)


def _has_sentence_boundary_between(
    kjv_sorted: list[KjvWord],
    lo_idx: int,
    hi_idx: int,
) -> bool:
    """True if any KJV word strictly between lo_idx and hi_idx (exclusive of
    lo, inclusive of hi-1) carries a sentence-terminating punctuation in
    its trailing punc. The CARRIER itself (hi-1) is included because punc
    at the end of a word severs the next-word from this-word.
    """
    if hi_idx <= lo_idx + 1:
        return False
    # Inspect every word from lo_idx (inclusive of its trailing punc) up to
    # but not including hi_idx.
    for k in range(lo_idx, hi_idx):
        punc = kjv_sorted[k].punc or ""
        for ch in punc:
            if ch in _SENTENCE_PUNCT:
                return True
    return False


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

    # KJV-index -> line index assignment (None if unassigned)
    assignment: list[int | None] = [None] * n_kjv
    claimed: list[bool] = [False] * n_kjv

    # Per-line anchor list: vpos values claimed by Strong's-tagged matches.
    # Built up over passes; used for positional-proximity decisions.
    per_line_anchors: list[list[int]] = [[] for _ in range(n_lines)]

    # Group source tokens by Strong's number with their (flat_idx, line_idx).
    # Also keep flat ordering: source line-index per flat position.
    src_strongs_occs: dict[str, list[tuple[int, int]]] = {}
    flat_idx = 0
    for line_idx, tokens in enumerate(source_tokens_per_line):
        for tok in tokens:
            for s in tok.strongs_list:
                src_strongs_occs.setdefault(s, []).append((flat_idx, line_idx))
            flat_idx += 1

    # Group KJV words by Strong's number with their (kjv_idx, vpos).
    kjv_strongs_occs: dict[str, list[tuple[int, int]]] = {}
    for kjv_idx, kw in enumerate(kjv_sorted):
        for s in kw.strongs_list:
            kjv_strongs_occs.setdefault(s, []).append((kjv_idx, kw.vpos))

    def _claim(kjv_idx: int, line_idx: int) -> None:
        if claimed[kjv_idx]:
            return
        claimed[kjv_idx] = True
        assignment[kjv_idx] = line_idx
        per_line_anchors[line_idx].append(kjv_sorted[kjv_idx].vpos)

    # Pass A1: Strong's with src_count <= kjv_count — monotonic 1:1.
    # Process all such Strong's first to seed anchors with maximum
    # confidence. Pass A2 then resolves the over-supplied cases using
    # the anchors A1 established.
    deferred_strongs: list[str] = []
    for s, src_occs in src_strongs_occs.items():
        kjv_occs = kjv_strongs_occs.get(s, [])
        if not kjv_occs:
            continue
        # Filter src_occs to dedupe per-line: if the same line has
        # multiple source tokens with the same Strong's (e.g. doubled
        # particle), still process them independently — they may all
        # legitimately claim distinct KJV occurrences.
        if len(src_occs) <= len(kjv_occs):
            # Monotonic 1:1, k-th src to k-th kjv.
            for k, (_, line_idx) in enumerate(src_occs):
                kjv_idx, _vpos = kjv_occs[k]
                if not claimed[kjv_idx]:
                    _claim(kjv_idx, line_idx)
        else:
            deferred_strongs.append(s)

    # Pass A2: over-supplied Strong's — positional-proximity per KJV occ.
    # For each KJV word with Strong's S, pick the source line (from those
    # that have a src-occurrence with S) whose A1 anchors are positionally
    # closest in KJV vpos. Ties: line nearest in source-line order.
    for s in deferred_strongs:
        src_occs = src_strongs_occs[s]
        kjv_occs = kjv_strongs_occs[s]
        # Lines that have at least one src-occurrence with this Strong's.
        candidate_lines = sorted({li for (_, li) in src_occs})
        # Assign each KJV occ to its positionally-nearest candidate line.
        # We do this in vpos order so that later assignments see updated
        # anchors. Not strictly necessary for correctness — anchors set
        # by A1 should dominate — but stable.
        for kjv_idx, vpos in kjv_occs:
            if claimed[kjv_idx]:
                continue
            line = _pick_line_by_proximity(
                vpos, candidate_lines, per_line_anchors, n_lines
            )
            _claim(kjv_idx, line)

    # Pass B: synonymy sweep. Any KJV word still unclaimed whose Strong's
    # overlap SOME source token in the verse. Used for cases like Greek
    # ἕξει -> "shall be with child" where the multi-KJV-word cluster
    # shares one source token's Strong's set.
    #
    # Candidate set: lines whose source has matching Strong's, PLUS any
    # line with an existing anchor at vpos ±1 (adjacency signal — when
    # the unclaimed vpos is contiguous with another line's claimed
    # range, that line is the natural KJV-flow extension even without
    # a Strong's source match). The adjacency-augmentation handles
    # cases like Matt 3:16 vpos 32 ("and lighting upon him") where
    # only one line had G2532 source but the right destination was
    # the adjacent line that owns vpos 33+ via other Strong's.
    for kjv_idx, kw in enumerate(kjv_sorted):
        if claimed[kjv_idx]:
            continue
        if not kw.strongs_list:
            continue
        candidate_lines: list[int] = []
        for s in kw.strongs_list:
            for _, li in src_strongs_occs.get(s, []):
                if li not in candidate_lines:
                    candidate_lines.append(li)
        # Adjacency augmentation: any line with an anchor at vpos±1
        for li in range(n_lines):
            if li in candidate_lines:
                continue
            if any(abs(a - kw.vpos) <= 1 for a in per_line_anchors[li]):
                candidate_lines.append(li)
        if not candidate_lines:
            continue  # no source overlap at all; falls to Pass D
        line = _pick_line_by_proximity(
            kw.vpos, sorted(candidate_lines), per_line_anchors, n_lines
        )
        _claim(kjv_idx, line)

    # Pass C: any KJV word still unassigned (translator-supplied OR
    # Strong's-tagged-with-no-source-overlap) attaches to the nearest
    # assigned neighbour. Forward preferred; if a sentence boundary
    # (".", "!", "?") sits between this word and its forward neighbour
    # but the backward neighbour is on the near side, prefer backward.
    # This keeps "And the Spirit of God moved" (after a period) attached
    # forward into the new sentence rather than backward to the prior one,
    # AND handles Strong's-tagged words whose source token's Strong's
    # set doesn't actually overlap any KJV row (a frequent MetaV/TAHOT
    # divergence for Hebrew pronominal suffixes like H9033, KJV H3240).
    for kjv_idx, kw in enumerate(kjv_sorted):
        if assignment[kjv_idx] is not None:
            continue
        # Forward look
        forward_assigned_idx: int | None = None
        for j in range(kjv_idx + 1, n_kjv):
            if assignment[j] is not None:
                forward_assigned_idx = j
                break
        # Backward look
        backward_assigned_idx: int | None = None
        for j in range(kjv_idx - 1, -1, -1):
            if assignment[j] is not None:
                backward_assigned_idx = j
                break

        forward_line = (
            assignment[forward_assigned_idx]
            if forward_assigned_idx is not None
            else None
        )
        backward_line = (
            assignment[backward_assigned_idx]
            if backward_assigned_idx is not None
            else None
        )

        chosen_line: int | None = None
        if forward_line is not None and backward_line is not None:
            # Sentence-boundary awareness: if there's a `.` / `!` / `?` in
            # the punctuation of any word at indices [kjv_idx, forward_idx)
            # OR [backward_idx, kjv_idx), that direction is "crossed."
            # Prefer the un-crossed direction.
            fwd_crosses = _has_sentence_boundary_between(
                kjv_sorted, kjv_idx, forward_assigned_idx
            )
            bwd_crosses = _has_sentence_boundary_between(
                kjv_sorted, backward_assigned_idx, kjv_idx
            )
            if fwd_crosses and not bwd_crosses:
                chosen_line = backward_line
            elif bwd_crosses and not fwd_crosses:
                chosen_line = forward_line
            else:
                # Default: forward.
                chosen_line = forward_line
        elif forward_line is not None:
            chosen_line = forward_line
        elif backward_line is not None:
            chosen_line = backward_line
        else:
            # No assigned neighbours anywhere — fallback line 0.
            chosen_line = 0
        assignment[kjv_idx] = chosen_line

    # Pass D: defensive fallback. Pass C should assign every KJV word, but
    # guard against any unassigned escapees by using global positional
    # proximity (or line 0 if no anchors exist anywhere).
    for kjv_idx, kw in enumerate(kjv_sorted):
        if assignment[kjv_idx] is not None:
            continue
        candidate_lines = list(range(n_lines))
        line = _pick_line_by_proximity(
            kw.vpos, candidate_lines, per_line_anchors, n_lines
        )
        assignment[kjv_idx] = line

    # Render: group by line, preserve KJV vpos order.
    per_line: list[list[KjvWord]] = [[] for _ in range(n_lines)]
    for kjv_idx, kw in enumerate(kjv_sorted):
        line = assignment[kjv_idx]
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
