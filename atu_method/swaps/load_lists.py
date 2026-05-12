"""Load and merge per-corpus swap lists.

Usage
-----
    from atu_method.swaps import load_corpus_swap_list, apply_swaps

    swap_pairs, quiet_set = load_corpus_swap_list("nt")
    html_line = apply_swaps(line, swap_pairs, quiet_set)

The function merges ``data/swaps/universal-kjv.json`` with the
corpus-specific file (``nt-archaisms.json`` or ``ot-archaisms.json``)
and returns a pre-sorted list ready for the swap engine cache.
"""

import json
from pathlib import Path

from .apply_swaps import build_sorted_swap_list

# Canonical location: atu-method/data/swaps/
_DATA_DIR = Path(__file__).parent.parent.parent / "data" / "swaps"

_CORPUS_FILES: dict[str, str] = {
    "nt": "nt-archaisms.json",
    "ot": "ot-archaisms.json",
}


def _load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _expand_case_variants(
    pairs: list[list[str]],
) -> list[tuple[str, str]]:
    """Expand each (archaic, modern) pair to include both lowercase and
    Capitalized forms, de-duplicating entries already present.

    The JSON files already include explicit capitalized variants for most
    entries, so this function serves as a safety net for any that were
    omitted.
    """
    seen: set[str] = set()
    result: list[tuple[str, str]] = []
    for archaic, modern in pairs:
        for a, m in [(archaic, modern), (archaic.capitalize(), modern.capitalize())]:
            if a not in seen:
                seen.add(a)
                result.append((a, m))
    return result


def load_corpus_swap_list(
    corpus: str,
) -> tuple[list[tuple[str, str]], set[str]]:
    """Load and merge universal + corpus-specific swap data.

    Parameters
    ----------
    corpus:
        One of ``"nt"`` or ``"ot"``.

    Returns
    -------
    swap_pairs:
        Pre-sorted list of (archaic, modern) tuples, longest-first.
        Pass directly to ``apply_swaps()`` and reuse the same list object
        on every call so the engine cache hits.
    quiet_set:
        Set of lowercase archaic strings that should receive the
        ``swap-quiet`` CSS class (no dotted underline).

    Raises
    ------
    ValueError
        If ``corpus`` is not one of the supported values.
    FileNotFoundError
        If the data files are not found at the expected path.
    """
    if corpus not in _CORPUS_FILES:
        raise ValueError(
            f"Unknown corpus {corpus!r}. Expected one of: {sorted(_CORPUS_FILES)}"
        )

    universal_path = _DATA_DIR / "universal-kjv.json"
    corpus_path = _DATA_DIR / _CORPUS_FILES[corpus]

    universal = _load_json(universal_path)
    corpus_data = _load_json(corpus_path)

    # Merge swap pairs (universal first, then corpus-specific)
    raw_pairs: list[list[str]] = list(universal.get("swaps", []))
    raw_pairs.extend(corpus_data.get("swaps", []))

    # Merge quiet sets
    quiet_lower: set[str] = set(q.lower() for q in universal.get("quiet", []))
    quiet_lower.update(q.lower() for q in corpus_data.get("quiet", []))

    # Expand case variants and sort longest-first
    expanded = _expand_case_variants(raw_pairs)
    sorted_pairs = build_sorted_swap_list(expanded)

    return sorted_pairs, quiet_lower
