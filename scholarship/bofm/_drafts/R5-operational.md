# R5 Operational Entry — Migration Draft

**This is a migration draft restructuring the current `readers-bofm/private/01-method/colometry-canon.md §5 Rule 5` entry into the MISRA-without-Rationale operational template** (per [`../../../docs/rule-template.md`](../../../docs/rule-template.md)). When approved, this content replaces the current §5 Rule 5 entry.

Comparison anchors:
- **Current state:** `readers-bofm/private/01-method/colometry-canon.md §5 Rule 5` (~10 lines mixing operational + grammatical-grounding prose)
- **Proposed restructured state:** the operational entry below (purely operational)
- **Extracted rationale:** [`../R5.md`](../R5.md) (full scholarship companion)

---

### R5: Equivalence "Or" as Appositive

**Status:** Active
**Category:** B (Editorial, judgment-required) — the substitution test is the discriminator and is not mechanically decidable for the general case; the validator routes corpus-attested patterns to STRONG-MERGE-CANDIDATE vs REVIEW-REQUIRED on a UD-detectable heuristic.
**Decidability:** UD-pattern for the STRONG branch (same-UPOS + short-conjunct heuristic); Discourse-context-needed for the REVIEW branch.
**Layer:** 3

**Rule.** A coordinating *or* connecting two semantically equivalent reformulations (the second restating the first in other words) is appositive — NOT a disjunction — and the two conjuncts together with the linking *or* MUST occupy a single v2-mine line. When the substitution test (replace *or* with *that is to say* or *in other words*; meaning preserved) succeeds, the construction is equivalence-*or* and MUST merge. When the substitution test fails, the *or* marks a genuine disjunction (two distinct alternatives) and the existing line treatment MUST be preserved (the rule does not fire). Cases where the substitution test is not mechanically decidable from UD signature alone MUST be routed to REVIEW-REQUIRED; the applier MUST NOT auto-merge REVIEW-bucket findings.

**UD signature.**
```yaml
trigger_equivalence_or:
  relation: cc
  form: or                     # surface form (case-insensitive); cc token's form
  attaches_to: second_conjunct_head
  second_conjunct_head:
    deprel: conj
    head: first_conjunct
  conjuncts_on_different_lines: true   # rule only fires when split
action: REVIEW                          # bucketed below by heuristic

heuristic_strong_merge:
  same_upos: true              # first_conjunct.upos == second_conjunct.upos
  any_of:
    - both_conjuncts_short_le_4_content_tokens
    - second_conjunct_short_le_4_content_tokens   # asymmetric-short second = canonical BoFM signal
  action: MERGE_COORDINATE_MEMBERS    # STRONG-MERGE-CANDIDATE bucket; auto-apply NOT authorized — see Category B

heuristic_review_required:
  conditions: cross-UPOS OR both_conjuncts_long
  action: REVIEW                # REVIEW-REQUIRED bucket; needs substitution-test editorial judgment
```

**Closed lists** (machine-readable).
```yaml
SHORT_CONJUNCT_THRESHOLD: 4    # non-PUNCT tokens in the conjunct's UD subtree

SUBSTITUTION_PROBES:           # used by human reviewer applying the substitution test
  - "that is to say"
  - "in other words"

# The rule has no closed-list lemma inventory; the conj-or surface form is the trigger.
# Bucketing into STRONG vs REVIEW is driven entirely by the structural heuristic.
```

**Scope.** Applies to a coordinating *or* tagged with UD `cc` whose head is a `conj` token, when the two conjuncts (the first being the head of the second's `conj` relation, the second being the head of the `cc` attachment) currently sit on different v2-mine lines. The rule governs MERGE candidacy only — when conjuncts already share a line the rule does not fire. The rule operates over the second-conjunct head's UD subtree (not its surface span) for the conjunct-size measurement; the SHORT_CONJUNCT_THRESHOLD counts non-PUNCT tokens.

**Exclusions (closed list — each cites dominating rule).**

1. Genuine disjunction (*or* marks two distinct alternatives, not a restatement; substitution test fails) → out of scope; existing line treatment preserved. Distinguished from equivalence-*or* by the substitution-test diagnostic in the rule statement.
2. Cross-UPOS conjuncts (e.g., NOUN-or-VERB, ADJ-or-PROPN) → REVIEW-REQUIRED bucket; cross-category coordination is rarely equivalence and almost always requires editorial judgment.
3. Both conjuncts long (each > `SHORT_CONJUNCT_THRESHOLD` content tokens) → REVIEW-REQUIRED bucket; long equivalence pairs are rare in BoFM and the substitution test cannot be confirmed from UD signature alone.
4. *Or*-coordinations functioning as compound objects under a shared verb or preposition (J1 compound-list members) → §1.4 J1 governs the head-and-object analysis; if the compound list reads as J1 series, R5 yields. The N=3+ cliff (§1.9) does not engage R5 because R5 fires only on N=2 *or*-pairs.
5. *Or*-coordinations inside a fixed idiom or formula → R18 governs.
6. *Or*-coordinations whose first conjunct ends at a Layer-1-prohibited line-final position (CCONJ, DET, AUX, ADP) → R9 / R11 / R12 / R13a Layer-1 vetoes win; the merge happens for the higher-tier reason and R5 is moot.

**Precedence.** §3.5 Tier 4 (default-merge precedence over split-triggers, M-override family). Yields to all Tier 1 (Layer 1) syntactic vetoes that would merge for an independent reason. Yields to Tier 2 (R18 fixed idiom, R15 vocative) inside their respective frames. Within Tier 4, R5 is parallel to M1 but operates on a different coordinator (*or* rather than *and*) and a different semantic relation (appositive equivalence rather than gorgianic bonded pair); the two rules do not collide on the same N=2 pair.

*Note:* §3.5 currently lists Tier 4 by M-override IDs (M1–M4) and does not enumerate R5; the precedence-consistency check during the BoFM canon migration will reconcile R5's tier placement. R5's operational behavior is structurally a Tier 4 merge-override (an apparent split-trigger — coordination on *or* — is overridden when the conjuncts are equivalence-related and the second restates the first).

**Examples.**

- *Compliant (STRONG-MERGE-CANDIDATE — same-UPOS, asymmetric-short second conjunct):* "and they have a part in the first resurrection, or have eternal life, being redeemed by the Lord" (Mosiah 15:24) — *or have eternal life* restates *have a part in the first resurrection*; substitution test passes (*that is to say, have eternal life*).
- *Compliant (STRONG-MERGE-CANDIDATE — same-UPOS, both short):* "the rod of iron, or the word of God" — *or the word of God* names the rod's referent; substitution test passes.
- *Non-compliant (R5 violation — equivalence-or split):* "and they have a part in the first resurrection, / or have eternal life" (the equivalence reformulation severed from its first conjunct).
- *Excluded — genuine disjunction:* "that he may live or die" — *or* marks two alternatives; substitution (*that is to say, die*) fails; R5 does not fire; existing line treatment preserved.
- *Excluded — cross-UPOS, routed to REVIEW:* a NOUN-or-VERB coordination requires editorial judgment of whether one names the other; UD signature alone cannot resolve.
- *Excluded — J1 compound-object reading:* an *or*-coordination functioning as a compound object under a shared verb falls under J1 compound-list-break-signals; R5 yields.

**Implementation.**

- Validator: [`validators/colometry/validate_rule_05_ud.py`](../../../../readers-bofm/validators/colometry/validate_rule_05_ud.py)
- Applier: not yet implemented (Category B status — STRONG-MERGE-CANDIDATE bucket awaits per-instance editorial confirmation via the substitution test before merge is applied)
- Closed-list / threshold definitions: `SHORT_CONJUNCT_THRESHOLD = 4` in validator source
- Bucketing logic: STRONG = same-UPOS ∧ (both-short ∨ second-short); REVIEW = otherwise
- Audit trail: `readers-bofm/private/audit-trail/R5.md` (to be populated during BoFM canon migration)
- Scholarship: [`../R5.md`](../R5.md)
