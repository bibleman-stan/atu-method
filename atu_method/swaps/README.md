# Swap System — Universal KJV Archaic Modernization

The swap system wraps archaic KJV tokens in HTML `<span>` markup so the
reader UI can toggle between the historical text and a modern equivalent.

## UX behaviour (identical across all three readers)

Default display: archaic form visible (e.g. `begat`, `thee`, `saith`).  
Modern pill toggled: `data-mod` replaces `data-orig` via CSS/JS.

Markup produced:

```html
<span class="swap" data-orig="begat" data-mod="fathered">begat</span>
```

High-frequency grammar archaisms (see `quiet` arrays in JSON files) get
no dotted underline decoration:

```html
<span class="swap swap-quiet" data-orig="thee" data-mod="you">thee</span>
```

## Data files

| File | Contents |
|---|---|
| `data/swaps/universal-kjv.json` | Archaisms common to both KJV NT and OT |
| `data/swaps/nt-archaisms.json` | NT-specific archaisms (begat, holpen, etc.) |
| `data/swaps/ot-archaisms.json` | OT-specific archaisms (firmament, begat, gat, etc.) |

Each file has two top-level keys:
- `"swaps"` — array of `["archaic", "modern"]` pairs
- `"quiet"` — array of lowercase archaic strings that receive no underline

Explicit capitalized variants are included in the JSON (e.g. `["Begat",
"Fathered"]`) so the swap engine can match sentence-initial tokens without
a separate case-folding pass.

## Universal vs. per-corpus split

Some archaisms are shared between the KJV NT and OT (`thee/thou/thy/ye`,
`hath/doth`, `saith`, `unto`, etc.). These live in `universal-kjv.json`.

Some archaisms are corpus-specific:
- `begat` appears in NT genealogies (Matt 1) and OT genealogies (Gen 5/10/11)
  — included in both `nt-archaisms.json` and `ot-archaisms.json`.
- `firmament` is OT-specific (Genesis creation account).
- `holpen` is NT-specific (Luke 1:54).
- `gat/drave/brake/sware` are OT-specific irregular pasts.

## `<the>` strip-not-swap policy (NT only)

TAGNT (the NT source treebank) uses angle-bracket notation `<the>` to mark
translator-supplied articles that have no Greek equivalent. These literal
angle-bracket strings must be **stripped before calling `apply_swaps()`**,
leaving plain `the` everywhere. Do not encode `<the>` as a swap entry —
the `<` and `>` characters would produce malformed HTML in the `data-orig`
attribute, and the angle-bracket form is a source-annotation convention,
not the text the reader should ever see.

Recommended strip in the NT build pipeline:

```python
import re
line = re.sub(r'<(the|a|an)>', r'\1', line)  # strip TAGNT insertions
```

## How downstream build pipelines consume this module

```python
from atu_method.swaps import apply_swaps, load_corpus_swap_list

# Load once; reuse the same list object for all lines (engine cache hit)
swap_pairs, quiet_set = load_corpus_swap_list("nt")  # or "ot"

for line in source_lines:
    line = apply_swaps(line, swap_pairs, quiet_set)
    # ... emit HTML
```

`load_corpus_swap_list` merges universal + corpus-specific data,
de-duplicates, expands case variants, and sorts longest-first so the
compiled regex engine prefers multi-word matches over substring matches.

## Source reference

Ported from `readers-bofm/build_book.py` (`apply_swaps()`, `build_swap_list()`).
BoFM-specific pre-passes (AICTP phrase swaps, do/does/doth collapse,
imperative+emphatic-pronoun drops) are intentionally not ported — they are
BoFM-style-specific and do not apply to NT/OT prose.
