"""Text-normalization helpers for corpus comparison (universal).

Two primary helpers:

1. `strip_punctuation(text, extra_chars=None)` — NFC-normalize and remove
   standard punctuation + Unicode variants. Callers can append corpus-specific
   sigla via `extra_chars`.

2. `strip_accents(text, accent_marks=DEFAULT_ACCENT_MARKS)` — NFD-decompose,
   remove combining accent marks (default: acute U+0301, grave U+0300,
   circumflex/perispomeni U+0342), NFC-recompose. Used for token-identity
   comparison when accentuation may diverge across parses (e.g. Greek
   enclitic sandhi). Breathing marks are NOT in the default set since they
   carry lexical weight (e.g. ἄγω vs ἅγιος).

Both helpers are pure functions; they do not mutate input.

Usage:
    from atu_method.parsing.normalize import strip_punctuation, strip_accents

    cleaned = strip_punctuation("Ἀβραάμ,")               # "Ἀβραάμ"
    comparable = strip_accents("ὁ")                      # "ο" with breathing kept
    # Greek-specific extension:
    cleaned_gk = strip_punctuation("Ἀβραάμ·", extra_chars="·⸀⸁⸂⸃⸄⸅")
"""

from __future__ import annotations

import re
import unicodedata


# Base punctuation set common across Latin/Greek/Hebrew corpora.
_BASE_PUNCT_CHARS = (
    r",.\;\s"
    r"'`\(\)\[\]\{\}—–"
    r":?!"
    r"·"   # middle dot
    r";"   # Greek question mark
    r"·"   # Greek ano teleia
    r"ʼ"   # modifier letter apostrophe
)


# Combining accent marks commonly stripped for cross-parse token comparison.
# Breathing marks (U+0313 smooth, U+0314 rough) are intentionally NOT in this
# default set because they carry lexical weight in Greek (e.g. ἄγω vs ἅγιος).
DEFAULT_ACCENT_MARKS = frozenset([
    "́",   # combining acute
    "̀",   # combining grave
    "͂",   # combining Greek perispomeni (circumflex)
])


def _compile_strip_re(extra_chars: str = "") -> re.Pattern:
    """Compile the strip-punctuation regex with optional extra characters."""
    pattern = f"[{_BASE_PUNCT_CHARS}{extra_chars}]"
    return re.compile(pattern, re.UNICODE)


# Cache compiled regexes per extra_chars value.
_STRIP_RE_CACHE: dict[str, re.Pattern] = {}


def strip_punctuation(text: str, extra_chars: str = "") -> str:
    """Strip punctuation and NFC-normalize.

    Strips the base set (comma, period, semicolon, whitespace, quotes,
    brackets, dashes, colon, question mark, exclamation, middle dot, Greek
    question mark + ano teleia, modifier apostrophe). Additional characters
    can be supplied via `extra_chars` (each character in the string is added
    to the strip set).

    Examples:
        strip_punctuation("Ἀβραάμ,")            # "Ἀβραάμ"
        strip_punctuation("τοῦ θεοῦ·", extra_chars="·⸀⸁⸂⸃⸄⸅")  # "τοῦ θεοῦ"
    """
    if extra_chars not in _STRIP_RE_CACHE:
        _STRIP_RE_CACHE[extra_chars] = _compile_strip_re(extra_chars)
    pattern = _STRIP_RE_CACHE[extra_chars]
    normalized = unicodedata.normalize("NFC", text)
    return pattern.sub("", normalized)


def strip_accents(
    text: str,
    accent_marks: frozenset[str] = DEFAULT_ACCENT_MARKS,
) -> str:
    """NFD-decompose, strip combining accents, NFC-recompose.

    Used for token-identity comparison when accentuation may diverge across
    parses (e.g. Greek enclitic sandhi). The default `accent_marks` set
    strips acute/grave/circumflex; breathing marks are preserved.

    Examples:
        strip_accents("ὁ")        # "ὁ" — breathing kept (smooth + omicron)
        strip_accents("τοῦ")      # "του" — circumflex stripped
    """
    decomposed = unicodedata.normalize("NFD", text)
    stripped = "".join(ch for ch in decomposed if ch not in accent_marks)
    return unicodedata.normalize("NFC", stripped)
