# R12 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 12` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 12 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 12` (Layer-1 cross-reference plus an inline extension carrying rationale + canonical-example + N=2-adjudication prose + grammatical-grounding citation)
- **Proposed restructured state:** the operational entry below (purely operational; two-profile structure)
- **Extracted rationale:** [`../R12.md`](../R12.md) (full scholarship companion)

---

### R12: Never Split Auxiliary from Main Verb

**Status:** Active
**Category:** A (Mechanical, mandatory)
**Decidability:** UD-pattern
**Layer:** 1 (simple AUX+V profile) / 3 (compound-verb-under-shared-auxiliary extension)

**Rule.** R12 has two operational profiles, both of which MUST be honored.

(a) **Simple AUX+V profile (Layer 1).** A line MUST NOT end on a token whose UPOS is `AUX` when that token has an `aux` relation to a `VERB` head on the following line. The two lines MUST be merged. Equivalently: a finite auxiliary MUST NOT be stranded from its main verb across a line boundary. This profile is generic English grammar and is enforced by the Layer 1 break-legality table.

(b) **Compound-verb-under-shared-auxiliary extension (Layer 3).** When a modal+auxiliary cluster (e.g., *could have*, *would have*, *shall have*, *had*, *hath*, *have been*) scopes via ellipsis over two or more coordinated participles distributed across line boundaries, the line carrying the dangling coordinated participle MUST be merged with the line carrying its shared auxiliary, subject to the N=2 adjudication below. The coordinated participles form one compound predicate under one shared auxiliary; stranding a coordinated participle from its shared auxiliary is forbidden.

**UD signatures.**
```yaml
trigger_simple_aux_v:
  relation: aux
  head: { upos: VERB }                       # main verb on line N+1
  dependent: { upos: AUX, line_position: line_final }   # AUX line-final on line N
action: MERGE_FORWARD

trigger_compound_verb_shared_aux:
  line_N:
    contains: { upos: AUX, lemma_in: MODAL_AUX_R12 }
    line_final: { upos: VERB, verbform_in: [Part, Ger] }   # past or -ing participle
  line_N_plus_1:
    starts_with: { upos: CCONJ, lemma: and }
    next: { upos: VERB, verbform_in: [Part, Ger] }
    contains_no: { dep_in: [nsubj, nsubj:pass] }
    contains_no_finite_verb: true
action: MERGE_FORWARD
```

**Closed lists** (machine-readable).
```yaml
MODAL_AUX_R12:
  modals:
    - may
    - might
    - shall
    - should
    - will
    - would
    - can
    - could
    - must
  perfect_have:
    - have
    - has
    - hath
    - hast
    - had
    - having
  be_aux:
    - is
    - are
    - was
    - were
    - art
    - am
    - be
    - been
    - being
  do_aux:
    - do
    - does
    - doth
    - did
  # Modal+aux clusters that scope as a unit over coordinated participles:
  # e.g. "could have", "would have", "shall have", "might have been"
  scope_clusters:
    - "<modal> have"
    - "<modal> have been"
    - "had"
    - "hath"
    - "have"
```

**Scope.** Profile (a) applies to every line-final `AUX` with an outgoing `aux` relation to a main `VERB` on the following line — independent of corpus register; it is generic English grammar. Profile (b) applies to BoFM-archaic compound-verb constructions where a single modal+auxiliary cluster on line N scopes elliptically across an *and*-coordinated participle on line N+1 that has neither its own subject nor its own finite verb. The dangling-participle line is structurally a coordinated participle, not a coordinate clause.

**Exclusions (closed list — each cites dominating rule).**

1. Line N+1 introduces an overt subject NP (`nsubj` or `nsubj:pass`) ahead of its verb → coordinate clause, not shared-auxiliary ellipsis; profile (b) does NOT fire (governed by J1).
2. Line N+1 contains its own finite verb (modal aux, perfect aux, or finite main verb) → coordinate finite clause; profile (b) does NOT fire (governed by J1).
3. Line N is a verse-header line (`\d+:\d+`) or other non-text line → out of scope.
4. Phrasal-verb particles tagged `compound:prt` are not auxiliaries — line-final particles are governed by Layer 1's compound:prt row, not this rule.
5. Archaic verb forms (*goeth*, *giveth*, *hath* as main lexical verb) misparsed as `AUX` when functioning as full lexical `VERB` — confirm via dependency direction before merging; out of scope when the token is the predication's main verb.

**Precedence.** §3.5 Tier 1 (Layer 1 syntactic veto) for profile (a). §3.5 Tier 4 (merge-overrides) for profile (b), governed by §3.5 Tier 6 N=2 adjudication when exactly two participles share the auxiliary. Wins over J1 at N=2 when the participles satisfy the M1 verb-synonymy test; yields to J1 at N≥3 unconditionally (§3.5.2 cliff). The N≥3 cliff is the same precedent across M1, R12, and R17.

**N=2 sub-rule (coordinated participles under shared auxiliary).** When profile (b) fires on exactly two coordinated participles under one shared modal+auxiliary, apply the §1.9 N=2 Adjudication Principle / M1 verb-synonymy test:

- Synonymous / cognate / intensification variants (*"rose and went"*, *"tried and failed"*, *"came and saw"*) → MERGE.
- Distinct non-synonymous actions, each with its own object or independent predicative force → SPLIT per J1 (each participle is its own atomic beat under the shared auxiliary).

At N≥3 coordinated participles under one shared auxiliary, J1 wins unconditionally (Helaman 3:16 six-verb-cascade precedent).

**Examples.**

- *Compliant — profile (a) MERGE:* "the people which shall / be brought to pass" → "the people which shall be brought to pass" (line-final `shall` with `aux` to following `brought`; merged).
- *Compliant — profile (b) MERGE (N=2, synonymous/cognate, Alma 12:26):* "could have gone forth and partaken of the tree of life" (one line; *could have* scopes over both participles; line 2 of the pre-merge state had no subject and no finite verb).
- *Compliant — profile (b) SPLIT (N=2, distinct non-synonymous, Alma 24:10):* "hath forgiven us of those our many sins and murders which we have committed, / and taken away the guilt from our hearts" (shared *hath* scopes over *forgiven* and *taken away*; the two actions are distinct non-synonymous with distinct objects; each earns its own atomic beat per J1).
- *Compliant — profile (b) SPLIT at N≥3 (Helaman 3:16 cliff):* coordinated participles at N≥3 under one shared auxiliary split into N lines, one per participle.
- *Non-compliant — profile (a) violation:* "could have / gone forth and partaken" (line-final *have* stranded from its participle; merge required).
- *Non-compliant — profile (b) violation:* "could have gone forth / and partaken of the tree of life" (dangling coordinated participle stranded from shared *could have*; subject and finite verb absent from line 2; merge required at N=2 cognate).
- *Excluded by Exclusion 1 (J1 governs):* "could have gone forth / and they partaken of the tree of life" (line N+1 introduces overt subject *they*; coordinate clause, not shared-auxiliary ellipsis).

**Implementation.**

- Validator (profile a): [`validators/syntax/validate_line_final_tokens.py`](../../../../readers-bofm/validators/syntax/validate_line_final_tokens.py) — checks line-final `AUX` with pending `aux` relation per Layer 1 break-legality table.
- Validator (profile b): [`validators/syntax/validate_rule_12_compound_verb.py`](../../../../readers-bofm/validators/syntax/validate_rule_12_compound_verb.py) — detects line-N modal+aux + line-final participle followed by line-N+1 *and* + bare participle without subject or finite verb.
- Layer 1 break-legality table: [`data/syntax-reference/ud-taxonomy.md` §7](../../../../readers-bofm/data/syntax-reference/ud-taxonomy.md) — rows *line-final `AUX` with pending `aux` relation* and *line-final participle followed by coordinated participle under shared modal+aux*, both marked `REQUIRED-MERGE`.
- Closed-list definitions: in validator source (`MODAL_AUX_PATTERN`, `PAST_PARTICIPLES`).
- Audit trail: `readers-bofm/private/audit-trail/R12.md` (to be populated during BoFM canon migration).
- Scholarship: [`../R12.md`](../R12.md).
