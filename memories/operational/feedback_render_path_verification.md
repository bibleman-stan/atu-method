---
name: render-path-verification
description: "Deploy-verify for browser-rendered artifacts MUST execute the render path (headless Chrome --dump-dom), not curl; and any data interpolated into markup MUST be escaped at the injection site — audit data values for markup-significant characters BEFORE shipping a renderer."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`87af68a0-0291-4910-962f-d0913b5722e6/85d82fb1064cff1f@v2`); state as of 2026-06-10 (snapshot mtime); possibly stale — re-verify before relying.


Two rule-gaps caught by Stan on the tanakh-morph launch (2026-06-06). The reader shipped
"live-verified" but Genesis 1 displayed 4 words: BHSA's gloss for את is the literal string
`<object marker>`, the template interpolated glosses into innerHTML unescaped, and the browser
parsed an unclosed `<object>` element that swallowed the rest of every chapter. The blast radius
was near-total: 46 angle-bracket glosses including `<relative>` (= אשר) and `<NEG>`, plus 3,178
ETCBC lemma translits (ayin = `<`).

**Why it shipped:** (1) my "live verify" was `curl` + grep — structurally incapable of seeing a
client-side render bug, since the chapter is rendered by JS from embedded JSON; the deploy-claim
rule was satisfied in letter, not substance. (2) The colliding data value was IN MY OWN earlier
probe output that session (`את | ... | <object marker>` in the Gen 1:1 BHSA dump) and I never
connected data-with-angle-brackets to an innerHTML renderer. Stan: "i am spending on you because
i expect you to be smart enough to figure all this stuff out on your own."

**How to apply:**

1. **Deploy-verify must exercise the same path the user's eyes use.** For any artifact whose
   content is client-side rendered (JS builds DOM from embedded data), verification = headless
   Chrome `--headless=new --dump-dom <url>` (executes the JS), then assert on the RENDERED DOM
   outside `<script>` blocks: expected structural counts (verse-blocks per chapter), zero
   injection artifacts (`<object`, unbalanced containers), spot content present (last verse
   marker). curl/grep on the static HTML only verifies the data shipped, not that it renders.
   Chrome path on this machine: `C:/Program Files/Google/Chrome/Application/chrome.exe`.

2. **Escape at every injection site, and audit the DATA for markup-significant characters
   before shipping any renderer.** When building a renderer over a corpus, enumerate the actual
   value space first (`grep` the data for `<>&"` — 30 seconds in TF/Python) instead of assuming
   "glosses are plain English". `esc()` on every `${...}` that carries data into innerHTML; the
   same audit applies to attribute contexts.

3. This generalizes the [[feedback_conformance_is_not_correctness]] shape to deploy-verification:
   a 200 + content-hash match is a proxy tick; reveal-by-RENDERING is the real check. And it
   extends verify-don't-recall: "the site works" is a state-claim about the rendered DOM, which
   must be observed, not inferred from the served bytes.

Fixed in readers-tanakh-morph commit bfdce60 (esc() at all interpolation sites + headless-Chrome
verification). Check the GREEK sibling for the same class: readers-gnt-morph's template also
innerHTML-renders glosses — MorphGNT/lexicon glosses need the same angle-bracket audit.
