# `atu_method.kjv_alignment`

Universal algorithm for distributing **KJV verbatim English** across
source-language **ATU lines** (atomic thought units) using
**Strong's-number matching**. Consumed by `readers-gnt` and
`readers-tanakh` so that both reader sites can render

- a Greek / Hebrew ATU line, and
- underneath it the KJV verbatim English that translates that line

without rewriting English word order to match the source language.

## The picture

User opens `gnt-reader.com/?source=kjv` and looks at Matt 1:2:

    Ἀβραὰμ ἐγέννησεν τὸν Ἰσαάκ,
    Abraham begat Isaac;

The English line is KJV verbatim — *not* "Abraham begat the Isaac" (a
naive interlinear) — because KJV's translators dropped the
definite article. KJV word order is preserved within each ATU line. The
English equivalent of `Μεθʼ ἡμῶν ὁ θεός.` is `God with us.` (KJV's
inversion), not "With us God".

## Algorithm

For each verse (run independently):

1. **Load KJV side from MetaV.** Per KJV word: text, trailing punctuation,
   list of Strong's tags. Words with no Strong's are translator-supplied
   ("italic" in KJV print).
2. **Load source side from caller.** Per source token: text, list of
   Strong's tags. Already split into ATU lines by the caller.
3. **First-match-wins claim pass.** Walk source tokens in order. For each
   token with non-empty Strong's, find the next unclaimed KJV word whose
   Strong's overlaps. Claim it for this token's line.
4. **Synonymy sweep.** Any KJV word still unclaimed with non-empty
   Strong's, but whose Strong's overlaps some source token in the verse,
   attaches to that source token's line. (Handles "one Greek aorist →
   multiple English words" cases like ἕξει → "shall be with child".)
5. **Translator-supplied attachment.** KJV words with no Strong's attach
   to the line of their nearest *forward* non-empty-Strong's neighbour
   (fallback: previous neighbour).
6. **Render.** Group by line, sort each line's KJV words by KJV
   verse-position, join with spaces, append punctuation from each word.

Correctness invariants per verse:
- Every KJV word appears on exactly one ATU line (no loss, no duplication).
- KJV verse-position order is preserved within each line.

## Public API

    from atu_method.kjv_alignment import (
        SourceToken,
        align_verse,
        normalize_strongs,
        extract_strongs_from_tagnt_col,
        extract_strongs_from_tahot_col,
        load_kjv_strongs_index,
        distribute_kjv_to_atu_lines,
    )

### Quick example (Matt 1:2, single ATU line)

    from pathlib import Path
    from atu_method.kjv_alignment import SourceToken, align_verse

    # Greek tokens for Matt 1:2 (in textual order) with their Strong's:
    tokens = [
        SourceToken("Ἀβραὰμ",     ("G11",)),
        SourceToken("ἐγέννησεν",  ("G1080",)),
        SourceToken("τὸν",        ("G3588",)),
        SourceToken("Ἰσαάκ",      ("G2464",)),
        SourceToken("Ἰσαὰκ",      ("G2464",)),
        SourceToken("δὲ",         ("G1161",)),
        # ...continue per TAGNT
    ]
    # Single ATU line in this example:
    result = align_verse(
        book_osis="Matt", chapter=1, verse=2,
        source_atu_lines_with_tokens=[tokens],
        metav_dir=Path("atu-method/data/kjv-strongs"),
    )
    # result == ["Abraham begat Isaac; and Isaac begat Jacob; ..."]

### Multi-line example (Matt 1:23)

    source_atu_lines_with_tokens = [
        [SourceToken("Ἰδοὺ", ("G2400",)), SourceToken("ἡ", ("G3588",)), ...],
        [SourceToken("καὶ", ("G2532",)), SourceToken("τέξεται", ("G5088",)), ...],
        # ...
        [SourceToken("Μεθʼ", ("G3326",)), SourceToken("ἡμῶν", ("G3165",)),
         SourceToken("ὁ", ("G3588",)), SourceToken("θεός", ("G2316",))],
    ]
    result = align_verse("Matt", 1, 23, source_atu_lines_with_tokens, metav_dir)
    # result[-1] == "God with us."

## Strong's normalization

`normalize_strongs()` accepts either-side raw forms and returns a list of
canonical base Strong's numbers (no leading zeros, no morphology suffix,
no alphabetic disambiguation suffix). Compound TAHOT cells like
`H9003/{H7225G}` expand to `["H9003", "H7225"]`. Comma-separated TAGNT
alt cells like `G3603, G2076` expand similarly. See module docstring for
full examples.

## Substrate / dependencies

- **viz.bible MetaV CSVs** at `atu-method/data/kjv-strongs/` for per-KJV-
  word Strong's tagging and surface form. License: CC-BY-SA 3.0.
  Attribution lives at `data/kjv-strongs/NOTICE.txt`.
- **STEPBible TAGNT / TAHOT** (in the consuming repos) for per-source-token
  Strong's tags. License: CC BY 4.0. Not bundled in this module — callers
  parse their own source-token data and pass `SourceToken` instances.
- Python stdlib only (`csv`, `re`, `dataclasses`, `pathlib`). No third-
  party runtime deps.

## Performance

First call to `load_kjv_strongs_index()` parses ~790k MainIndex rows and
~325k StrongsIndex rows. Wall time ~3-6 seconds on a typical workstation.
Result is cached in a module-level dict so subsequent calls are O(1).
Memory footprint ~195 MB resident for the full 31k-verse index (790k
KjvWord instances). Each verse alignment after load is sub-millisecond.

## License

Code: MIT (this module).
MetaV data: CC-BY-SA 3.0 (Steve Tice / viz.bible).
TAGNT/TAHOT data (not bundled here): CC BY 4.0 (STEPBible / Tyndale
House).
