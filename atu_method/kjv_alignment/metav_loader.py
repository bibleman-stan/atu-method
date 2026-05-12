"""MetaV CSV loader (cached, verse-indexed).

Parses viz.bible's MetaV CSVs once and returns an in-memory dict keyed by
(book_id, chapter, verse) -> [KjvWord, ...] in KJV reading order.

Substrate: atu-method/data/kjv-strongs/{MetaV_MainIndex.csv, MetaV_StrongsIndex.csv}
License: CC-BY-SA 3.0 (viz.bible / Steve Tice et al.). Attribution in
data/kjv-strongs/NOTICE.txt.

Notes on the MetaV data:
- MainIndex has one row per KJV word with Word, Punc, Italic, VersePos.
- StrongsIndex joins WordID -> StrongsID with one row per Strong's tag
  (a single KJV word may carry 0, 1, or N Strong's tags).
- The Italic column is unused (all zero) in the public CSV release. The
  actual signal for translator-supplied words is empty Strong's list.
- BookID is 1..66 in canonical order; we expose BOOK_ID_TO_OSIS / inverse.
"""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path

# Bump CSV field-size cap; MetaV cells are small but defensive.
csv.field_size_limit(10**7)

# 66-book OSIS-prefix mapping. MetaV uses BookID 1..66 in canonical order;
# OSIS labels per the de-facto convention used by MetaV's OsisRef column
# (NT: "Matt", "Mark", "Luke", "John", "Acts", "Rom", "1Cor", "2Cor", ...).
BOOK_ID_TO_OSIS: dict[int, str] = {
    1: "Gen", 2: "Exod", 3: "Lev", 4: "Num", 5: "Deut",
    6: "Josh", 7: "Judg", 8: "Ruth",
    9: "1Sam", 10: "2Sam", 11: "1Kgs", 12: "2Kgs",
    13: "1Chr", 14: "2Chr",
    15: "Ezra", 16: "Neh", 17: "Esth",
    18: "Job", 19: "Ps", 20: "Prov", 21: "Eccl", 22: "Song",
    23: "Isa", 24: "Jer", 25: "Lam", 26: "Ezek", 27: "Dan",
    28: "Hos", 29: "Joel", 30: "Amos", 31: "Obad", 32: "Jonah",
    33: "Mic", 34: "Nah", 35: "Hab", 36: "Zeph",
    37: "Hag", 38: "Zech", 39: "Mal",
    40: "Matt", 41: "Mark", 42: "Luke", 43: "John",
    44: "Acts",
    45: "Rom", 46: "1Cor", 47: "2Cor", 48: "Gal", 49: "Eph",
    50: "Phil", 51: "Col", 52: "1Thess", 53: "2Thess",
    54: "1Tim", 55: "2Tim", 56: "Titus", 57: "Phlm",
    58: "Heb", 59: "Jas", 60: "1Pet", 61: "2Pet",
    62: "1John", 63: "2John", 64: "3John", 65: "Jude", 66: "Rev",
}
OSIS_TO_BOOK_ID: dict[str, int] = {v: k for k, v in BOOK_ID_TO_OSIS.items()}
# Also accept readers-gnt's TAGNT three-letter prefixes (Mat/Mrk/Luk/Jhn/...)
# as aliases — common downstream convention.
TAGNT_TO_OSIS: dict[str, str] = {
    "Mat": "Matt", "Mrk": "Mark", "Luk": "Luke", "Jhn": "John",
    "Act": "Acts", "1Co": "1Cor", "2Co": "2Cor",
    "Phi": "Phil", "Php": "Phil", "Col": "Col",
    "1Th": "1Thess", "2Th": "2Thess",
    "1Ti": "1Tim", "2Ti": "2Tim",
    "Tit": "Titus", "Phm": "Phlm",
    "Jas": "Jas", "1Pe": "1Pet", "2Pe": "2Pet",
    "1Jn": "1John", "2Jn": "2John", "3Jn": "3John",
    "Jud": "Jude", "Rev": "Rev",
}


@dataclass(frozen=True)
class KjvWord:
    """One KJV word in MetaV reading order.

    Attributes:
        text: surface form ("In", "beginning", "Behold")
        punc: trailing punctuation as stored by MetaV (",", ".", ";", "")
        italic: True if KJV-italic-translator-supplied. In MetaV the column
            is unused; we treat empty strongs_list as the operative signal,
            but we expose the raw italic flag here for completeness.
        strongs_list: normalised base Strong's numbers (may be empty)
        vpos: VersePos (0-based KJV reading order within verse)
        word_id: MetaV WordID (stable global ID, for debugging)
    """

    text: str
    punc: str
    italic: bool
    strongs_list: tuple[str, ...]
    vpos: int
    word_id: int

    @property
    def is_translator_supplied(self) -> bool:
        """True if this word has no Strong's tag (treat as KJV italic)."""
        return len(self.strongs_list) == 0

    def render(self) -> str:
        """Render text + trailing punctuation as KJV prints it."""
        return f"{self.text}{self.punc}"


KjvIndex = dict[tuple[int, int, int], list[KjvWord]]


# Module-level cache so consumers can call load_kjv_strongs_index multiple
# times with the same metav_dir and only pay the parse cost once.
_CACHE: dict[Path, KjvIndex] = {}


def _normalize_one_strongs(raw: str) -> str | None:
    """Strip leading zeros + suffix on a MetaV StrongsID cell ("G0846", "H7225G")."""
    if not raw:
        return None
    raw = raw.strip()
    if not raw:
        return None
    prefix = raw[0]
    if prefix not in ("H", "G"):
        return None
    rest = raw[1:]
    digits = ""
    for ch in rest:
        if ch.isdigit():
            digits += ch
        else:
            break
    if not digits:
        return None
    return f"{prefix}{int(digits)}"


def load_kjv_strongs_index(
    metav_dir: Path | str, *, use_cache: bool = True
) -> KjvIndex:
    """Load the full KJV-with-Strong's index from MetaV CSVs.

    Parses MetaV_MainIndex.csv + MetaV_StrongsIndex.csv. Returns a dict
    keyed by (book_id, chapter, verse) with list-of-KjvWord values in
    KJV reading order (sorted by VersePos ascending).

    First call: ~3-6 seconds on a typical workstation (~790k MainIndex rows
    + ~325k StrongsIndex rows). Subsequent calls return the cached result.

    Args:
        metav_dir: directory containing MetaV_MainIndex.csv and
            MetaV_StrongsIndex.csv.
        use_cache: if True (default), reuse a prior in-memory parse.
    """
    metav_dir = Path(metav_dir)
    if use_cache and metav_dir in _CACHE:
        return _CACHE[metav_dir]

    main_path = metav_dir / "MetaV_MainIndex.csv"
    strongs_path = metav_dir / "MetaV_StrongsIndex.csv"
    if not main_path.is_file():
        raise FileNotFoundError(f"MetaV MainIndex not found: {main_path}")
    if not strongs_path.is_file():
        raise FileNotFoundError(f"MetaV StrongsIndex not found: {strongs_path}")

    # Pass 1: WordID -> list of normalised Strong's
    word_strongs: dict[int, list[str]] = {}
    with strongs_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                wid = int(row["WordID"])
            except (KeyError, ValueError):
                continue
            s = _normalize_one_strongs(row.get("StrongsID", ""))
            if s is None:
                continue
            word_strongs.setdefault(wid, []).append(s)

    # Pass 2: MainIndex -> per-verse list of KjvWord
    index: KjvIndex = {}
    with main_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                book_id = int(row["BookID"])
                chapter = int(row["Chapter"])
                verse = int(row["VerseNum"])
                vpos = int(row["VersePos"])
                word_id = int(row["WordID"])
            except (KeyError, ValueError):
                continue
            text = row.get("Word", "") or ""
            punc = row.get("Punc", "") or ""
            italic = (row.get("Italic", "0") or "0") == "1"
            slist = word_strongs.get(word_id, [])
            # Dedup while preserving order (StrongsIndex may have duplicates)
            seen: set[str] = set()
            normalized: list[str] = []
            for s in slist:
                if s not in seen:
                    seen.add(s)
                    normalized.append(s)
            kw = KjvWord(
                text=text,
                punc=punc,
                italic=italic,
                strongs_list=tuple(normalized),
                vpos=vpos,
                word_id=word_id,
            )
            index.setdefault((book_id, chapter, verse), []).append(kw)

    # Final pass: sort each verse's words by VersePos
    for key, words in index.items():
        words.sort(key=lambda w: w.vpos)

    if use_cache:
        _CACHE[metav_dir] = index
    return index


def resolve_book_osis(book_osis_or_alias: str) -> str:
    """Resolve a possibly-aliased book token (TAGNT 'Mat' -> OSIS 'Matt')."""
    if book_osis_or_alias in OSIS_TO_BOOK_ID:
        return book_osis_or_alias
    if book_osis_or_alias in TAGNT_TO_OSIS:
        return TAGNT_TO_OSIS[book_osis_or_alias]
    raise KeyError(f"Unknown book OSIS or alias: {book_osis_or_alias!r}")


def book_id_for_osis(book_osis_or_alias: str) -> int:
    """Return MetaV BookID for an OSIS book code or TAGNT alias."""
    return OSIS_TO_BOOK_ID[resolve_book_osis(book_osis_or_alias)]


# Allow `python -m atu_method.kjv_alignment.metav_loader path/to/metav` for
# quick smoke-tests during development.
if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) < 2:
        print("usage: metav_loader.py <metav_dir>", file=sys.stderr)
        sys.exit(2)
    idx = load_kjv_strongs_index(sys.argv[1])
    print(f"loaded {len(idx)} verses")
    sample = idx[(1, 1, 1)]
    for w in sample:
        print(f"  vpos={w.vpos} word={w.text!r}{w.punc!r} strongs={w.strongs_list}")
