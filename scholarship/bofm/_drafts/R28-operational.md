# R28 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 28` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 28 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 28` (~10 lines mixing operational + rationale content under the Grammatical-basis / UD-signature / Diagnostic / Example template)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R28.md`](../R28.md) (full scholarship companion)

---

### R28: Speech-Act Announcement After Frame

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** UD-pattern
**Layer:** 3

**Rule.** A speech verb's matrix predication (subject + finite speech verb + colon-introduced quote) MUST be split from a preceding scene-setting adverbial frame when (a) the speech verb's lemma is in `SPEECH_LEMMAS_R28`, (b) the verb carries an `nsubj` dependent, and (c) the verb has an `advcl` sibling (or direct `advcl` dependent) whose mark lemma is in `FRAME_MARK_LEMMAS`. The break MUST be inserted before the leftmost non-PUNCT token of the speech-clause subtree that follows the rightmost advcl-subtree token on the line; any trailing frame-closing comma stays on the frame line. Participial speech-continuation advcl (`saying`-headed) and result/comparative advcl MUST NOT trigger this rule.

**UD signature.**
```yaml
trigger:
  relation: advcl                # advcl as sibling-of or dependent-of the speech verb
  head: { upos: VERB, lemma_in: SPEECH_LEMMAS_R28 }
  head_deps: { nsubj: required }
  mark: { lemma_in: FRAME_MARK_LEMMAS }
action: SPLIT_BEFORE_SUBJECT
```

**Closed lists** (machine-readable).
```yaml
SPEECH_LEMMAS_R28:
  - say
  - speak
  - declare
  - cry
  - answer

FRAME_MARK_LEMMAS:
  - after
  - when
  - while
  - before
  - since
  - until
  - because
  - though
  - although
  - lest
  - except

ADVCL_EXCLUDED_LEMMAS:        # participial speech-continuation, not a frame
  - say                       # surface form "saying"

RESULT_MARK_LEMMAS:           # consequence-not-frame when speech precedes advcl
  - that
  - insomuch
  - until
```

**Scope.** Same-line co-occurrence of a matrix speech-VERB (with `nsubj`) and a genuine scene-setting frame-advcl on a single v2-mine line. The detector compares the v2-mine line of the speech VERB to the line of the advcl root; only same-line co-occurrence (verb_line == advcl_line) is in scope. Speech verbs as parataxis dependents of the AICTP "pass" verb are in scope — Rule 28 applies regardless of whether the speech verb is the sentence root or a parataxis dependent.

**Exclusions (closed list — each cites dominating rule).**

1. Participial speech-continuation `, saying:` — advcl lemma in `ADVCL_EXCLUDED_LEMMAS`; not a scene-setting frame → out of scope.
2. Comparative `as if` advcl (both *as* and *if* present as marks) — comparative clause, not a scene frame → out of scope.
3. Result-direction inversion: speech verb token id < advcl token id AND mark lemma in `RESULT_MARK_LEMMAS` — the advcl is a consequence of the speech act, not a frame preceding it → out of scope.
4. Bare `aux:pass` participial advcl without temporal/locative mark AND without true-absolute construction (own `nsubj` differing from the matrix `nsubj`) — manner-circumstantial, not a frame → out of scope.
5. No-clean-split-col case: speech-tag structurally inside (or before) the advcl on the line, with no non-PUNCT speech-only token following `advcl_end_id` → REVIEW-REQUIRED (not auto-applied).
6. Direct discourse already on its own line (verb_line ≠ advcl_line) — already conformant; no split needed.

**Precedence.** §3.5 Tier 5. Co-instantiates J3 (speech-act announcement) at the matrix-predication level. No yields-to relationships against higher-tier rules are known to fire on the same trigger.

**Examples.**

- *Compliant (SPLIT):* "And it came to pass that after Aaron had expounded these things unto him, / the king said:" (Alma 22:15) — frame *after Aaron had expounded these things unto him,* ends with comma on the frame line; matrix *the king said:* begins the next line.
- *Compliant (saith-the-Lord parenthetical authentication-stamp):* "for I have a great work to do, / saith the Lord" — speech tag on its own line after intervening matrix.
- *Non-compliant (R28 violation — frame and speech-tag merged):* "And it came to pass that after Aaron had expounded these things unto him, the king said:" (single line — frame and announcement on the same v2-mine line).
- *Excluded by Exclusion 1 (saying-continuation, MERGE):* "he spake unto them, saying:" — *saying* is a participial speech-continuation marker, not a scene-setting frame.
- *Excluded by Exclusion 3 (result-direction inversion):* "I did speak many words unto them, / that they were pacified" — speech verb precedes advcl and mark is *that* (result); the advcl is the consequence of the speech act, not its frame.
- *Excluded by Exclusion 4 (manner-circumstantial passive):* "being filled with the Spirit, he spake" — bare `aux:pass` participial advcl without temporal/locative mark and without distinct own-subject; manner-circumstantial, not a frame → out of R28 scope.
- *Excluded by Exclusion 5 (REVIEW-REQUIRED):* "Ye cannot say, when ye are brought to that awful crisis," (Alma 34:34) — speech-tag is structurally inside the advcl; no clean split column.

**Implementation.**

- Validator: [`validators/colometry/validate_rule_28_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_28_ud.py)
- Applier: [`validators/apply_rule_28_ud.py`](../../../../readers-bofm/validators/apply_rule_28_ud.py)
- Closed-list definitions: in validator source (`SPEECH_LEMMAS`, `FRAME_MARK_LEMMAS`, `ADVCL_EXCLUDED_LEMMAS`, `RESULT_MARK_LEMMAS`)
- Char-offset emission: detector emits `split_col` via `build_line_map_full`; applier inserts the break before `split_col` (T1.1 char-offset pattern).
- Audit trail: `readers-bofm/private/audit-trail/R28.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R28.md`](../R28.md)
