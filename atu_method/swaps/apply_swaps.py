"""Universal swap-application engine for KJV-style archaic modernization.

Ported from readers-bofm/build_book.py apply_swaps(). BoFM-specific
pre-passes (AICTP hiding, do/does/doth collapse, AICTP phrase swaps,
imperative+emphatic-pronoun drops) are intentionally NOT ported — they
are BoFM-style-specific and do not apply to NT or OT prose.

The universal engine handles:
  - Multi-word swaps sorted longest-first (greedy match)
  - Word-boundary matching via regex
  - Quiet class for high-frequency grammar archaisms (no dotted underline)
  - Case-preserving output: the archaic form is the visible default display
  - HTML span markup: <span class="swap" data-orig="{a}" data-mod="{m}">{a}</span>
"""

import re


# ---------------------------------------------------------------------------
# Module-level compiled-engine cache
# ---------------------------------------------------------------------------
_SWAP_ENGINE_CACHE: dict = {}


def _build_engine(swap_list: list[tuple[str, str]]) -> tuple:
    """Build a compiled regex + lookup dict for the given swap list.

    Returns (compiled_regex, lookup_dict).
    """
    lookup: dict[str, str] = {}
    patterns: list[str] = []
    seen: set[str] = set()

    for archaic, modern in swap_list:
        if archaic in seen:
            continue
        seen.add(archaic)
        lookup[archaic] = modern
        patterns.append(re.escape(archaic))

    # Sort longest-first so alternation prefers longer/multi-word matches
    patterns.sort(key=len, reverse=True)

    # Build one alternation: \b(?:pattern1|pattern2|...)\b
    big_pattern = r'\b(?:' + '|'.join(patterns) + r')\b'
    compiled = re.compile(big_pattern)
    return compiled, lookup


def _get_engine(swap_list: list[tuple[str, str]]) -> tuple:
    """Return a cached (compiled_regex, lookup) for the given swap list.

    Cache key is a tuple of the swap pairs (hashable), not id(), so the
    cache is content-addressable and survives across list object lifetimes.
    """
    key = tuple(swap_list)
    if key not in _SWAP_ENGINE_CACHE:
        _SWAP_ENGINE_CACHE[key] = _build_engine(swap_list)
    return _SWAP_ENGINE_CACHE[key]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def apply_swaps(
    text: str,
    swap_list: list[tuple[str, str]],
    quiet_set: set[str] | None = None,
) -> str:
    """Wrap archaic tokens in HTML swap spans.

    Parameters
    ----------
    text:
        Input text line (plain text, may already contain HTML from earlier
        processing — existing markup is not double-wrapped because the
        word-boundary regex will not match tokens already inside a span).
    swap_list:
        List of (archaic, modern) tuples. Will be sorted longest-first
        internally if not already sorted. Pass a pre-sorted list for
        best performance on repeated calls (use the same list object so
        the engine cache hits).
    quiet_set:
        Set of lowercase archaic strings that should receive the
        ``swap-quiet`` CSS class (no dotted underline). If None, all
        swaps use the plain ``swap`` class.

    Returns
    -------
    str
        Text with archaic tokens replaced by::

            <span class="swap" data-orig="{archaic}" data-mod="{modern}">{archaic}</span>

        or with ``class="swap swap-quiet"`` for quiet archaisms.

    Notes
    -----
    The swap engine uses a single compiled regex alternation for
    performance. Sentinel placeholders prevent double-replacement when
    a shorter archaic token overlaps with an already-matched longer one.
    """
    if quiet_set is None:
        quiet_set = set()

    placeholders: list[tuple[str, str, str]] = []
    result = text

    compiled_re, lookup = _get_engine(swap_list)

    def _replace(m: re.Match) -> str:
        matched = m.group(0)
        # Guard: skip if we are inside an already-placed sentinel
        start = m.start()
        window = result[max(0, start - 2):start]
        if '\x00' in window:
            return matched
        modern = lookup.get(matched)
        if modern is None:
            return matched
        idx = len(placeholders)
        sentinel = f"\x00G{idx}\x00"
        placeholders.append((sentinel, matched, modern))
        return sentinel

    result = compiled_re.sub(_replace, result)

    # Expand sentinels → HTML spans
    for sentinel, archaic, modern in placeholders:
        arc_low = archaic.lower()
        is_quiet = arc_low in quiet_set
        css_class = 'swap swap-quiet' if is_quiet else 'swap'
        span = (
            f'<span class="{css_class}" '
            f'data-orig="{archaic}" '
            f'data-mod="{modern}">'
            f'{archaic}</span>'
        )
        result = result.replace(sentinel, span)

    return result


def build_sorted_swap_list(
    swap_pairs: list[tuple[str, str]],
) -> list[tuple[str, str]]:
    """Return swap_pairs sorted longest-first (required for greedy matching).

    Call this once when constructing the swap list, then pass the sorted
    list to apply_swaps() repeatedly so the engine cache hits every time.
    """
    return sorted(swap_pairs, key=lambda x: len(x[0]), reverse=True)


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    failures = 0

    def check(label: str, got: str, expected: str) -> None:
        global failures
        if got == expected:
            print(f"  PASS  {label}")
        else:
            print(f"  FAIL  {label}")
            print(f"        got:      {got!r}")
            print(f"        expected: {expected!r}")
            failures += 1

    print("Running apply_swaps self-tests...")

    # Test 1: basic single-word swap
    result1 = apply_swaps("Abraham begat Isaac;", [("begat", "fathered")])
    check(
        "basic single-word swap",
        result1,
        'Abraham <span class="swap" data-orig="begat" data-mod="fathered">begat</span> Isaac;',
    )

    # Test 2: quiet class
    result2 = apply_swaps("thee", [("thee", "you")], {"thee"})
    check(
        "quiet class",
        result2,
        '<span class="swap swap-quiet" data-orig="thee" data-mod="you">thee</span>',
    )

    # Test 3: multi-word longest-first preference
    swap_list_3 = build_sorted_swap_list([
        ("it came to pass that", "then"),
        ("it came to pass", "then it happened"),
    ])
    result3 = apply_swaps("it came to pass that", swap_list_3)
    check(
        "multi-word longest-first",
        result3,
        '<span class="swap" data-orig="it came to pass that" data-mod="then">it came to pass that</span>',
    )

    # Test 4: case preservation — "Begat" stays capitalized in data-orig
    result4 = apply_swaps("Begat", [("Begat", "Fathered")])
    check(
        "case preservation (capitalized form)",
        result4,
        '<span class="swap" data-orig="Begat" data-mod="Fathered">Begat</span>',
    )

    # Test 5: no match — text unchanged
    result5 = apply_swaps("Abraham fathered Isaac;", [("begat", "fathered")])
    check(
        "no match — text unchanged",
        result5,
        "Abraham fathered Isaac;",
    )

    # Test 6: multiple swaps in one string
    result6 = apply_swaps(
        "hath begat",
        build_sorted_swap_list([("hath", "has"), ("begat", "fathered")]),
    )
    check(
        "multiple swaps in one string",
        result6,
        '<span class="swap" data-orig="hath" data-mod="has">hath</span> '
        '<span class="swap" data-orig="begat" data-mod="fathered">begat</span>',
    )

    print()
    if failures == 0:
        print(f"All tests passed.")
    else:
        print(f"{failures} test(s) FAILED.")
        sys.exit(1)
