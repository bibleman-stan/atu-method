# Scholarship — Per-Rule Rationale Companions

This directory holds **rationale, grammatical grounding, empirical evidence, and intellectual lineage** for each rule in each per-corpus canon. It is the companion document to the per-repo `private/01-method/colometry-canon.md` §5 (Rule Detail).

The audience for this directory is the **scholar** — reviewer, peer, dissertation reader, future researcher applying the apparatus to a new corpus. The audience for the operational canon is the **robot** (LLM agent, validator code, fresh-session Claude doing the work). The two audiences have zero overlap in needs:

| Audience | Needs | Document |
|---|---|---|
| Operational (robot) | WHAT the rule is, HOW signed, WHERE applies, WHAT excludes, WHICH wins, examples | Per-repo canon §5 |
| Scholarly (human) | WHY the rule exists, WHY this framing defensible, WHAT precedents ground it, HOW empirically validated | This directory |

---

**Status: SCAFFOLD** — to be populated by extraction from per-repo canon rule entries (the "Grammatical basis", "WHY", "HOW WE KNOW", "Corpus empirics", "Grammatical grounding" content currently embedded inside §5 rule bodies).

---

## File organization

Per-corpus subdirectories hold per-rule scholarship files:

```
scholarship/
├── _index.md                  This file.
├── bofm/                      BoFM rule scholarship.
│   ├── R7.md                  Rule 7 (Purpose Clauses) rationale.
│   ├── R17.md                 Rule 17 (Complement Integrity) rationale.
│   └── ...
├── gnt/                       GNT rule scholarship.
│   ├── R8.md
│   ├── R9.md
│   └── ...
└── tanakh/                    Tanakh rule scholarship.
    ├── H7.md
    └── ...
```

Per-rule scholarship files contain:

1. **Statement** (one sentence — the operational rule this scholarship supports).
2. **Rationale** (the WHY — why the rule's framing is defensible).
3. **Grammatical grounding** (citations to CGEL / BDF / Joüon-Muraoka / Smyth / Wallace / Wickes / etc.).
4. **Empirical evidence** (corpus counts, sweep results that validate the rule's TP rate).
5. **Intellectual lineage** (who / what / when produced this framing; cross-project provenance).
6. **Adversarial history** (what failure modes the rule was designed to prevent; what scope-claims were considered and rejected).
7. **Future work** (open questions; what next-phase discourse infrastructure would change about the rule).

Scholarship entries are dense — ~50–200 lines per rule — and version slowly. They are the published-quality methodology documentation that a peer-review paper would cite.

---

## Universal scholarship (not per-rule)

Cross-cutting methodology essays live in `scholarship/methodology/`:

- `methodology/framework.md` — the WHY behind §1 (proposition-first, structural justifications, merge-overrides).
- `methodology/categories.md` — the WHY behind §2 Category A/B/C.
- `methodology/precedence.md` — the WHY behind the BoFM canon §3.5 (and analogous per-corpus precedence hierarchies).
- `methodology/lineage.md` — Skousen / BoFM / GNT / Tanakh intellectual lineage.
- `methodology/audit-discipline.md` — the WHY behind §7.3 mandatory-audit triggers.

These essays are the venue where the framework's defensibility lives. They are the publication-ready material.

---

**This scaffold will be populated by extraction in subsequent releases.**
