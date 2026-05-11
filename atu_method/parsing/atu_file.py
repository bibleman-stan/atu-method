"""ATU-per-line file format loader (universal).

The "ATU file" format is the v2-mine / v4-editorial / similar plain-text
shape used across reader editions:

    1:1
    First atomic thought unit of the chapter
    Second atomic thought unit
    1:2
    First ATU of verse 2
    ...

Each non-empty line is either:
- A verse-number marker (matching `^\\d+:\\d+$`)
- An ATU content line belonging to the current verse

Blank lines are ignored.

The loader returns AtuChapter holding AtuLine items in chapter-order with
0-based line_index, the verse_ref each line belongs to, and (optionally)
punctuation-stripped tokens.

This module is corpus-agnostic. Per-corpus directory-layout glue (resolving
a (book, chapter) pair to a file path on disk) lives in the consuming repo
and calls into load_atu_chapter with the resolved path.

Usage:
    from atu_method.parsing.atu_file import (
        AtuLine, AtuChapter, load_atu_chapter, VERSE_NUM_RE,
    )

    chapter = load_atu_chapter(
        filepath="data/text-files/v4-editorial/01-matt/matt-04.txt",
        book_display="Matt",
        chapter_num=4,
        tokenize=my_tokenizer,  # optional: callable[[str], list[str]]
    )
    for line in chapter.lines:
        print(line.verse_ref, line.line_index, line.text)
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional


VERSE_NUM_RE = re.compile(r"^\s*\d+:\d+\s*$")


@dataclass
class AtuLine:
    """One ATU line in a chapter.

    line_index: 0-based across the whole chapter (not per-verse).
    verse_ref:  display form e.g. "Matt 4:1" (caller-formatted).
    text:       raw line content with trailing whitespace stripped.
    tokens:     optional list of punctuation-stripped tokens.
    """
    line_index: int
    text: str
    verse_ref: str
    tokens: list[str] = field(default_factory=list)


@dataclass
class AtuChapter:
    """One chapter's worth of ATU lines."""
    book: str            # display form (e.g. "Matt", "1Cor")
    chapter: int
    lines: list[AtuLine] = field(default_factory=list)


def parse_atu_text(
    text: str,
    book_display: str,
    chapter_num: int,
    tokenize: Optional[Callable[[str], list[str]]] = None,
) -> AtuChapter:
    """Parse ATU-file text (raw string) into an AtuChapter.

    See load_atu_chapter for the file-format spec.
    """
    chapter = AtuChapter(book=book_display, chapter=chapter_num, lines=[])
    current_verse_ref = f"{book_display} {chapter_num}:?"  # fallback before first marker
    line_index = 0

    for raw in text.splitlines():
        stripped = raw.rstrip()
        if not stripped.strip():
            continue
        m = VERSE_NUM_RE.match(stripped)
        if m:
            # Extract "ch:vs" from the marker — strip whitespace for safety.
            marker = stripped.strip()
            current_verse_ref = f"{book_display} {marker}"
            continue
        tokens = tokenize(stripped) if tokenize is not None else []
        chapter.lines.append(AtuLine(
            line_index=line_index,
            text=stripped,
            verse_ref=current_verse_ref,
            tokens=tokens,
        ))
        line_index += 1

    return chapter


def load_atu_chapter(
    filepath: str | Path,
    book_display: str,
    chapter_num: int,
    tokenize: Optional[Callable[[str], list[str]]] = None,
) -> AtuChapter:
    """Load an ATU-file from disk and parse it into an AtuChapter.

    Args:
        filepath: path to the ATU file (UTF-8 plain text).
        book_display: display name for the book (e.g. "Matt", "Alma").
        chapter_num: integer chapter number.
        tokenize: optional callable(line_text) -> list[str] producing
            punctuation-stripped tokens per line. If omitted, AtuLine.tokens
            is left empty.

    Returns AtuChapter with 0-based line indices and verse_ref populated.
    """
    text = Path(filepath).read_text(encoding="utf-8")
    return parse_atu_text(text, book_display, chapter_num, tokenize=tokenize)
