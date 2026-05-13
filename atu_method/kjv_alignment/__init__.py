"""Universal KJV-distribution-by-Strong's algorithm.

Given a list of source-language ATU lines (each line a list of source tokens
with attached Strong's numbers) and the KJV verbatim words for the verse
(with per-word Strong's tags from viz.bible MetaV), distribute KJV words to
ATU lines preserving KJV verse order within each line.

Consumed by readers-gnt and readers-tanakh in Wave 5c: each repo's
regenerate_english_kjv extractor becomes a thin wrapper that loads its own
source-token data (TAGNT/TAHOT) and calls into this module.

Substrate:
- viz.bible MetaV CSVs (CC-BY-SA 3.0) at atu-method/data/kjv-strongs/ for
  per-KJV-word Strong's tagging and Italic flagging
- STEPBible Strong's lexicons (TBESG/TBESH) are bundled in atu-method/
  data/lexicons/ for downstream consumer use; this module does not
  consult them.

Public API:
- KjvWord, SourceToken: dataclasses for the two sides of the alignment
- normalize_strongs(raw): canonicalise a Strong's tag from either source
- load_kjv_strongs_index(metav_dir): build verse-indexed MetaV structure
- distribute_kjv_to_atu_lines(source_tokens_per_line, kjv_words): the core
- align_verse(book_osis, chapter, verse, source_atu_lines_with_tokens,
  metav_dir): convenience high-level call
"""

from atu_method.kjv_alignment.distribute import (
    KjvWord,
    SourceToken,
    distribute_kjv_to_atu_lines,
)
from atu_method.kjv_alignment.metav_loader import (
    BOOK_ID_TO_OSIS,
    OSIS_TO_BOOK_ID,
    KjvIndex,
    load_kjv_strongs_index,
)
from atu_method.kjv_alignment.strongs_normalize import (
    extract_strongs_from_tagnt_col,
    extract_strongs_from_tahot_col,
    normalize_strongs,
)
from atu_method.kjv_alignment.api import align_verse

__all__ = [
    "KjvWord",
    "SourceToken",
    "KjvIndex",
    "BOOK_ID_TO_OSIS",
    "OSIS_TO_BOOK_ID",
    "normalize_strongs",
    "extract_strongs_from_tagnt_col",
    "extract_strongs_from_tahot_col",
    "load_kjv_strongs_index",
    "distribute_kjv_to_atu_lines",
    "align_verse",
]
