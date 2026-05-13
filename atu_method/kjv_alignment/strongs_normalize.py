"""Strong's-number normalization.

The viz.bible MetaV dataset and the STEPBible TAGNT/TAHOT datasets both use
H/G-prefixed Strong's numbers but with different formatting conventions:

- MetaV         "G846", "H7225"                (no leading zeros, no suffix)
- TAGNT col 4   "G0846=P-GSM"                  (zero-padded, =morphology)
- TAGNT col 12  "G0846"                        (zero-padded, bare)
- TAGNT col 13  "G3603, G2076"                 (comma-separated alternates)
- TAHOT col 5   "H9003/{H7225G}"               (compound w/ braces + suffix)
- TAHOT col 9   "H7225G"                       (alphabetic disambiguation)

To match across these we normalise to a canonical form:
- Strip braces      {H1254A} -> H1254A
- Strip morphology  G1080=V-AAI-3S -> G1080
- Strip suffix      H7225G -> H7225  (any trailing [A-Z])
- Strip zero-pad    G0846 -> G846

Compound source-tokens (TAHOT "H9003/{H7225G}") expand to a LIST of base
Strong's numbers. Some compounds are KJV-untranslatable particle codes
(H9001..H9050 range — definite article, conjunction, preposition prefixes,
etc.) but we keep them in the list for completeness; the matching step
naturally drops them because MetaV has no rows with those Strong's.
"""

from __future__ import annotations

import re


_SUFFIX_RE = re.compile(r"^([HG])0*(\d+)([A-Z]?)$")


def normalize_strongs(raw: str) -> list[str]:
    """Normalise one raw Strong's cell to a list of base Strong's numbers.

    Examples:
        "{H1254A}"            -> ["H1254"]
        "G1080=V-AAI-3S"      -> ["G1080"]
        "G0846"               -> ["G846"]
        "H9003/{H7225G}"      -> ["H9003", "H7225"]
        "G3603, G2076"        -> ["G3603", "G2076"]
        "G2455N=N-NSM-P"      -> ["G2455"]
        ""                    -> []
        "H7225"               -> ["H7225"]
    """
    if not raw:
        return []
    out: list[str] = []
    # Split on slash (TAHOT compound), backslash (TAHOT trailing meta-codes
    # like \H9016 verse-end and \H9018 section marker), comma (TAGNT alt
    # list), and whitespace.
    parts = re.split(r"[/\\,\s]+", raw.strip())
    for part in parts:
        if not part:
            continue
        # Strip braces
        token = part.strip().lstrip("{").rstrip("}")
        # Strip everything after = (morphology)
        if "=" in token:
            token = token.split("=", 1)[0]
        # Now token should be H#### or G#### with optional zero-pad + suffix
        m = _SUFFIX_RE.match(token)
        if m:
            prefix, digits, _suffix = m.groups()
            out.append(f"{prefix}{int(digits)}")
        # Otherwise unparseable — silently skip
    # Preserve order but dedup
    seen: set[str] = set()
    deduped: list[str] = []
    for s in out:
        if s not in seen:
            seen.add(s)
            deduped.append(s)
    return deduped


# TAGNT vs MetaV/KJV-Strong's lemma-variant equivalences.
# TAGNT uses the "newer" Strong's numbering for some lemmas where the
# original Strong's tagging (used by KJV/MetaV) lists a variant. These
# pairs name the SAME Greek word but disagree on the canonical Strong's
# tag. Without explicit equivalence, Pass A1 exact-Strong's-match fails
# even though the source word semantically maps to the KJV translation.
#
# Each entry: canonical Strong's number → set of equivalent Strong's
# (membership is bidirectional once expanded below).
_LEMMA_EQUIVALENTS_RAW: dict[str, set[str]] = {
    # ἔπω / ἐρῶ / ῥέω suppletive paradigm — all "say" (Matt 21:3, etc.)
    "G2036": {"G2046", "G4483"},
    # πραΰτης / πραότης — meekness alternate spelling (Gal 5:23)
    "G4240": {"G4236"},
    # μόνος (adj) / μόνον (adv) — alone/only (Gal 6:12)
    "G3441": {"G3440"},
}


def _build_lemma_equivalents() -> dict[str, frozenset[str]]:
    """Build bidirectional equivalence map from _LEMMA_EQUIVALENTS_RAW.

    Returns {strongs -> frozenset(all equivalents including self)}.
    """
    union: dict[str, set[str]] = {}
    for primary, equivs in _LEMMA_EQUIVALENTS_RAW.items():
        cluster = {primary, *equivs}
        for s in cluster:
            union.setdefault(s, set()).update(cluster)
    return {s: frozenset(c) for s, c in union.items()}


_LEMMA_EQUIVALENTS: dict[str, frozenset[str]] = _build_lemma_equivalents()


def expand_lemma_equivalents(strongs: list[str]) -> list[str]:
    """Expand a Strong's list with known lemma-variant equivalents.

    For each Strong's number, add any registered equivalents (TAGNT vs
    KJV/MetaV tagging divergences). Preserves input order; equivalents
    appended after the original tag they expanded from.
    """
    out: list[str] = []
    seen: set[str] = set()
    for s in strongs:
        if s not in seen:
            seen.add(s)
            out.append(s)
        for eq in _LEMMA_EQUIVALENTS.get(s, ()):
            if eq not in seen:
                seen.add(eq)
                out.append(eq)
    return out


def extract_strongs_from_tagnt_col(cell4: str, cell12: str = "", cell13: str = "") -> list[str]:
    """Extract Strong's from TAGNT row.

    cell4  = primary Strong's + morphology (e.g. "G1080=V-AAI-3S")
    cell12 = primary Strong's bare         (e.g. "G1080")     [optional]
    cell13 = KJV-alternate Strong's        (e.g. "G3603, G2076") [optional]

    Returns a deduplicated list of base Strong's numbers covering primary,
    alternates, and known lemma-variant equivalents (see
    _LEMMA_EQUIVALENTS_RAW). The alternates from cell13 are essential for
    matching KJV words whose Strong's tagging diverges from TAGNT's
    primary lemma (e.g. εἰμί G1510 in TAGNT vs. KJV "is" G2076). The
    lemma-equivalents handle cases where TAGNT uses one Strong's variant
    for a lemma and KJV uses another (Matt 21:3 ἐρεῖτε G4483 vs "say" G2046).
    """
    out: list[str] = []
    seen: set[str] = set()
    for raw in (cell4, cell12, cell13):
        for s in normalize_strongs(raw):
            if s not in seen:
                seen.add(s)
                out.append(s)
    return expand_lemma_equivalents(out)


def extract_strongs_from_tahot_col(cell5: str, cell9: str = "") -> list[str]:
    """Extract Strong's from TAHOT row.

    cell5 = compound Strong's (e.g. "H9003/{H7225G}")
    cell9 = primary content-word Strong's (e.g. "H7225G") [optional]

    Returns a deduplicated list. cell5 is the canonical source; cell9 is a
    fallback for noisy cell5 cases.
    """
    out: list[str] = []
    seen: set[str] = set()
    for raw in (cell5, cell9):
        for s in normalize_strongs(raw):
            if s not in seen:
                seen.add(s)
                out.append(s)
    return out
