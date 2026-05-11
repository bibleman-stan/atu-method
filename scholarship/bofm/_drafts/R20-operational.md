# R20 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 20` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 20 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 20` (mixed operational + grammatical-basis + corpus-status content)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R20.md`](../R20.md) (full scholarship companion)

---

### R20: No-Anchor Rule

**Status:** Active
**Category:** B (Editorial, judgment-required) — violation diagnosis is mechanical; remediation (MERGE_FORWARD vs. restructure) requires per-case judgment
**Decidability:** UD-pattern
**Layer:** 3

**Rule.** Every v2-mine line MUST carry at least one thought-marking anchor. An anchor is one of: a finite `VERB`, an infinitival `VERB`, a `VERB` participle functioning predicatively on the line, or a substantive head independently predicated on the line via an attached `cop` or own predicate. A line containing zero anchors MUST be remediated by merging forward with the next line, unless the line satisfies one of the four exemptions in §Exemptions below. Bare noun-phrases that continue a prior line's predicate as object continuations or appositional extensions do NOT count as anchors regardless of their nominal content.

**UD signature.**
```yaml
trigger:
  line: { anchor_count: 0 }
  excludes:
    - { exemption: single_line_verse }
    - { exemption: speech_intro_prefix }
    - { exemption: standalone_sentence_connective }
    - { exemption: passes_structural_justification }  # any of J1-J5
action: MERGE_FORWARD  # default remediation
# When MERGE_FORWARD would violate another rule, or when the line's role
# requires restructure rather than merge, action is REVIEW.
```

**Closed lists** (machine-readable).
```yaml
ANCHOR_KINDS:
  - finite_VERB              # tensed verb with nsubj or imperative
  - infinitival_VERB         # to-infinitive heading its own predication on the line
  - predicative_participle   # VERB participle functioning as predicate of the line
  - substantive_with_cop     # NP head with attached cop / own predicate on the line

NON_ANCHOR_NOMINALS:
  - object_continuation       # bare NP continuing prior line's verb's obj
  - apposition_extension      # bare NP appositional to prior line's NP
  - coordinate_object_member  # bare "and [NP]" member of a compound object list

STANDALONE_SENTENCE_CONNECTIVES:
  - Wherefore
  - And now
  - Therefore
  - Now
  - Yea
  - Behold
```

The `STANDALONE_SENTENCE_CONNECTIVES` list captures discourse connectives that legitimately occupy their own line in BoFM register as scene-setters, even though they carry no verbal anchor. Membership is constrained to corpus-attested cases.

**Scope.** Every v2-mine line is in scope. The rule operates after all generative split-triggers (Tier 5) and merge-overrides (Tier 4) have settled — it is a floor-check that catches lines produced by the upstream pipeline (or by hand-editing) that lack predicative content. The rule does NOT govern line content beyond anchor presence; lines with one or more anchors are not further constrained by R20.

**Exemptions (closed list — each cites dominating rule or framework justification).**

1. **Single-line verses** — verses whose v2-mine representation is exactly one line are atomic by definition and pass R20 regardless of internal anchor count. → out of scope
2. **Speech-intro prefixes** — short colon-terminated or paratactically-introducing speech tags (e.g., bare *saying:*, *and he said:*) — the speech-act announcement IS the predication, even when the surface anchor is elided → J3
3. **Standalone sentence connectives** — discourse connectives from `STANDALONE_SENTENCE_CONNECTIVES` legitimately occupy their own line as scene-setting beats → J3 / J5
4. **Lines passing any structural justification** — lines without a verbal anchor that nevertheless pass one of the five structural justifications via formal-structural recoverability (parallel-series member with elided shared predicate, portrait-accumulation stack-member, classical comma, substantive adjunct as own focus) → J1 / J2 / J3 / J4 / J5

**Precedence.** §3.5 Tier 8. Floor-check that fires after all Tier 1-7 rules have settled. Yields to every upstream tier when an upstream rule's output places a no-anchor line on the page — R20 then either remediates by MERGE_FORWARD or routes to REVIEW when remediation would violate an upstream rule.

**Examples.**

- *Compliant (finite VERB anchor):* "And he did minister unto them" — anchor: finite `VERB` *minister* with `nsubj` *he*
- *Compliant (predicative participle anchor):* "I, Nephi, having been born of goodly parents" — anchor: predicative participle *born* (the participial-absolute predication; R21 territory)
- *Compliant (substantive-with-cop anchor):* "the records were of great worth" — anchor: NP *the records* + attached `cop` *were*
- *Compliant (exemption — single-line verse):* a verse rendered as exactly one v2-mine line, even if it contains no surface VERB → out of scope per Exemption 1
- *Compliant (exemption — standalone connective):* "Wherefore" on its own line introducing a new discourse beat → Exemption 3 (J3 / J5)
- *Compliant (exemption — J1 series member):* "and the brass plates," as a member of a parallel object series under an elided shared predicate → Exemption 4 (J1 compound-list)
- *Non-compliant (zero anchors, no exemption applies):* "and also her mistress, the queen, and the king," as a standalone line — three bare NPs in object-continuation of a prior line's verb; no anchor; no exemption fires → MERGE_FORWARD with the next line OR restructure per editorial review
- *Non-compliant (zero anchors, mid-stream):* a bare prepositional phrase line like "in the wilderness" not functioning as a J5 substantive adjunct on its own focus → MERGE_FORWARD with its matrix line

**Implementation.**

- Validator: [`validators/syntax/validate_rule_20_ud.py`](../../../../readers-bofm/validators/syntax/validate_rule_20_ud.py)
- Applier: not implemented (remediation is per-case editorial — R20 violations route to MERGE_FORWARD candidate or REVIEW; no auto-applier)
- Closed-list definitions: `ANCHOR_KINDS`, `STANDALONE_SENTENCE_CONNECTIVES` in validator source
- Audit trail: `readers-bofm/private/audit-trail/R20.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R20.md`](../R20.md)
