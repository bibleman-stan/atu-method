# Toolset Architecture — Mechanical-First Pipeline

This document specifies the pipeline implementation. The framework spec (`framework.md` §3) defines the v0→v3 stages; this document specifies WHAT each stage runs.

The pipeline is **mechanical-first**: parse-derived clause units are merged into ATU candidate groups by feature-driven binding rules. LLM adjudication is OPTIONAL and narrow-task. Editorial review handles residuals.

---

## v0 — Source text

Per-corpus canonical text with verse markers:

| Corpus | Source | Path convention |
|---|---|---|
| Tanakh | Westminster Leningrad Codex (WLC) | `data/text-files/v0/prose/{book-folder}/{book-stem}.txt` |
| GNT | SBLGNT | `data/text-files/v4/grk/{book-folder}/{book-stem}.txt` |
| BoFM | 2020 LDS Book of Mormon | `data/text-files/v2-mine/{book-folder}/{book-stem}.txt` |
| LXX (planned) | Rahlfs-Hanhart | TBD |
| Vulgate (planned) | Stuttgart | TBD |

The v0 file is verse-level (one verse per paragraph, headed by `BB:NN` verse marker). No pre-applied segmentation.

## v1 — Parse-derived clauses

Each language uses its own parse layer:

| Corpus | Parse layer | Clause unit | Tooling |
|---|---|---|---|
| Hebrew | BHSA (ETCBC) | `clause_atom` | Text-Fabric |
| Greek | Macula Greek (Clear-Bible) | clause node | XML / direct read |
| EME English | Stanza CoNLL-U | sentence | parsed directly |
| Latin (planned) | UD-Latin or LDT | clause | UD tools |

For Hebrew specifically, v1 extracts each `clause_atom` with these features:
- `cid` — BHSA node id
- `verse` — chapter:verse
- `typ` — clause type (Way0, WayX, WXQt, xQt0, Voct, Defc, NmCl, etc.)
- `rela` — relation to mother clause (Cmpl, Attr, Adju, etc.)
- `head_verb_lemma` — lemma of clause's predicating verb
- `text` — pointed Hebrew text

Output: JSONL with one record per parse-derived clause, in document order.

## v1.5 — Binding rules

A small catalog of binding rules merges adjacent v1 clauses into ATU candidate groups. Each rule:

- Fires based on parse-derived features (clause type, head lemma, text-prefix after pointing-strip)
- Is justified by the bidirectional test
- Operates only within a single verse (no cross-verse binding)

For Hebrew, see [`binding-rules-hebrew.md`](binding-rules-hebrew.md) for the 14 validated rules (B1-B14, with B4 retired).

Output: JSONL with one record per ATU candidate group + binding-history per group.

## v2 — LLM adjudication (optional)

When the mechanical layer's output diverges from editorial expectation on specific patterns (e.g., length-dependent restrictive ʾăšer), narrow LLM calls can adjudicate:

- One call per ambiguous group, with 2-3 prior groups as context
- Single yes/no question (e.g., "how many ATUs in this group, with which split points?")
- 3 independent passes; aggregate to UNANIMOUS / MAJORITY / ALL-DISAGREE

The LLM does **not** do chapter-level rendering. Its scope is narrow per-group adjudication on flagged residuals.

For pilots and validated chapters, the mechanical layer alone is publishable. v2 is reserved for production scaling where edge cases recur.

**Dispatch options:**
- Direct API call via `anthropic` SDK (requires `ANTHROPIC_API_KEY`)
- Agent-dispatch from a host Claude Code session (no external API key needed)

## v3 — Editorial review

The editor sees:
- The mechanical-first ATU group sequence (v1.5 output)
- Any v2 LLM verdicts on residuals
- Flagged-uncertain cases

Editor produces the final ATU rendering, committed to the corpus's `data/text-files/v2/` (or equivalent).

For chapters where the editor has produced a hand-validated rendering, v0-v2 serve as a comparison cross-check (see `v3_three_way_compare.py` in the pilot).

---

## Coarse-anchor principle

The mechanical signal should be the COARSEST reliable signal. Finer signals (te'amim, editorial punctuation) are informational, not adjudicative.

| Signal | Role |
|---|---|
| Versification | Hard upper bound on ATU spans (no ATU crosses a verse) |
| Parse-derived clauses (BHSA / Macula / CoNLL-U) | Primary mechanical unit (clause-atom) |
| Te'amim / cantillation | Informational (performance/breathing anchors, not cognitive) |
| Editorial punctuation (KJV, Stephanus, Masoretic) | Calibration evidence at audit time only; not piped into pipeline |
| Strong's / TAHOT / TAGNT alignment | English-layer rendering (separate concern from ATU segmentation) |

---

## Pilot artifacts

The pilot scripts at `readers-tanakh/research/atu-pilot-mechanical-first/` are the reference implementation:

| Script | Stage |
|---|---|
| `build_baseline_docx.py` | Generates 3-layer cold-eye docx (Hebrew / transliteration / KJV) |
| `v1_extract_clauses.py` | v0 → v1 (BHSA clause-atom extraction) |
| `v1_5_apply_bindings.py` | v1 → v1.5 (binding rules applied) |
| `v2_llm_atu_judgments.py` | v1.5 → v2 (Opus 3-pass; optional) |
| `v3_three_way_compare.py` | Compare pipeline / cold-eye / LDHB |
| `parse_ldhb.py` | Parse LDHB markup for calibration |
| `pilot_config.py` | Single source of truth for chapter selection |

Each script reads from `pilot_config.py` for chapter-specific paths. To run on a new chapter: edit `pilot_config.py`'s 5 lines (BOOK_NAME, CHAPTER_NUM, BOOK_FOLDER, BOOK_FILE_STEM, CHAPTER_DISPLAY).

---

## Productization (TODO)

The pilot scripts are research-quality. Productizing for full-corpus rendering requires:

1. **Batching across chapters** — currently config is single-chapter; needs orchestration
2. **Integration with `refresh_book.py` cascade** — automatic v0→v2/heb pipeline triggering
3. **Regression fixtures** — per-binding-rule test cases
4. **Cost / time monitoring** — for any v2 LLM scale-up

These are engineering moves, not methodology moves. The methodology is settled.

---

## Cross-references

- [`framework.md`](framework.md) — methodology specification
- [`binding-rules-hebrew.md`](binding-rules-hebrew.md) — the 14 Hebrew binding rules
- [`apparatus.md`](apparatus.md) — scope statement
- [`methodology-position.md`](methodology-position.md) — LDHB relationship
