"""Convenience high-level API.

Composes the metav_loader and distribute steps for the common single-verse
alignment call. Wave 5c consumer scripts (readers-gnt + readers-tanakh
regenerate_english_kjv.py) call into this.
"""

from __future__ import annotations

from pathlib import Path

from atu_method.kjv_alignment.distribute import (
    SourceToken,
    distribute_kjv_to_atu_lines,
)
from atu_method.kjv_alignment.metav_loader import (
    book_id_for_osis,
    load_kjv_strongs_index,
)


def align_verse(
    book_osis: str,
    chapter: int,
    verse: int,
    source_atu_lines_with_tokens: list[list[SourceToken]],
    metav_dir: Path | str,
) -> list[str]:
    """Align KJV verbatim words to source ATU lines for one verse.

    Args:
        book_osis: book label, either OSIS ("Matt", "Gen", "1Cor") or
            TAGNT alias ("Mat", "1Co").
        chapter: 1-based chapter number.
        verse: 1-based verse number.
        source_atu_lines_with_tokens: one inner list per source-language
            ATU line, each containing SourceToken instances in textual
            order. Empty inner lists are allowed (will render as empty
            string in output; caller decides on a placeholder).
        metav_dir: path to atu-method/data/kjv-strongs (containing
            MetaV_MainIndex.csv + MetaV_StrongsIndex.csv).

    Returns:
        list of KJV strings (one per ATU line, same order). KJV verbatim,
        KJV vpos-ordered within each line. Empty string for lines with no
        claimed KJV words.

    Raises:
        KeyError: if the verse is not present in MetaV.
    """
    index = load_kjv_strongs_index(metav_dir)
    book_id = book_id_for_osis(book_osis)
    key = (book_id, chapter, verse)
    if key not in index:
        raise KeyError(f"Verse not in MetaV: {book_osis} {chapter}:{verse} (BookID={book_id})")
    kjv_words = index[key]
    return distribute_kjv_to_atu_lines(source_atu_lines_with_tokens, kjv_words)
