# ATU Method

> Computational colometry apparatus for revealing atomic thought units in
> canonical texts.

**Status:** Pre-release (0.1.0) — repository scaffold established; content
extraction in progress from the proof-of-concept implementation in
[readers-bofm](https://github.com/bibleman-stan/readers-bofm).

---

## What this is

ATU Method is a methodology and Python infrastructure for producing
**colometric reading editions** of canonical texts. Each line on the page
renders one atomic thought unit (ATU) — a span of text a reader can take in
as a single unit of meaning before needing the next.

The apparatus implements a **proposition-first generative principle** with
five structural justifications and four merge-overrides, validated against
Universal Dependencies (UD) parse data and TEI-style scholarly-editing
conventions.

## Reader editions

This repository provides shared infrastructure consumed by per-corpus reader
editions:

- [**readers-bofm**](https://github.com/bibleman-stan/readers-bofm) — Book
  of Mormon (BoFM). The proof-of-concept implementation; reference for
  patterns used here.
- [**readers-gnt**](https://github.com/bibleman-stan/readers-gnt) — Greek
  New Testament (GNT), consuming Macula-Greek + MorphGNT parse data.
- [**readers-tanakh**](https://github.com/bibleman-stan/readers-tanakh) —
  Hebrew Bible (Tanakh), consuming Macula-Hebrew + BHSA/ETCBC parse data.

## Architecture

Four planes, separated by concern (not stacked by abstraction level):

| Plane | What lives there |
|---|---|
| **Data plane** | Per-repo: source texts, parsed corpora, edited corpora, transaction logs. |
| **Specification plane** | Shared in this repo: framework (§0/§1/§2/§7), glossary, rule-template, discipline memories. Per-repo: language-specific rule detail (§5), language-specific syntax-floor tables. |
| **Tooling plane** | Shared in this repo: parsing primitives, parse-data adapters, applier base classes, transaction logging, dashboard runner, parity-test framework, audit-extension hooks. |
| **Delivery plane** | Per-repo: build pipelines, reader web UIs, audio/morph/study overlays. |

See [`docs/architecture.md`](docs/architecture.md) for the full
decomposition with interface contracts between planes.

## Repository structure

```
atu-method/
├── atu_method/              Python package (importable)
│   ├── parsing/             UD query primitives, char-offset line mapping
│   ├── adapters/            Macula-lowfat-XML and CoNLL-U adapters
│   ├── infrastructure/      TxLog, rollback, applier base, dashboard, parity
│   ├── hooks/               Audit-extension git-hook helpers
│   └── english/             Archaic-English swap engine (BoFM + KJV)
├── docs/                    Shared specifications
│   ├── apparatus.md         High-level system overview
│   ├── architecture.md      Four-plane architecture + interface contracts
│   ├── framework.md         §0 Mission / §1 Framework / §2 Categories / §7 Protocol
│   ├── glossary.md          ATU, J1–J5, M1–M4, N=2 adjudication, etc.
│   ├── rule-template.md     Operational-canon rule-spec template
│   └── change-protocol.md   §7.3 mandatory-audit triggers, audit-evidence rules
├── memories/                Cross-project discipline lessons (~17 captured patterns)
├── scholarship/             Per-rule rationale and grammatical-grounding companions
└── tests/                   Unit tests for the Python package
```

## Installation

Pre-release; not yet on PyPI. Install from a local clone:

```bash
git clone https://github.com/bibleman-stan/atu-method.git
cd atu-method
pip install -e .
```

Reader editions consume the package via editable install:

```bash
cd /path/to/readers-bofm
pip install -e /path/to/atu-method
```

## Attribution

This work is open-licensed (MIT for code, CC-BY-4.0 for documentation). Both
licenses require attribution. The preferred citation form is:

> Stan the Bible Man. *ATU Method: Computational Colometry for Canonical Texts.*
> 2026. https://github.com/bibleman-stan/atu-method

For machine-readable citation, see [`CITATION.cff`](CITATION.cff)
(auto-rendered by GitHub's "Cite this repository" widget).

If you apply this methodology to a new corpus, please cite it in any
resulting publication or repository. Adaptations and extensions are welcomed
under the licenses; we ask only that credit be preserved.

## License

- **Code** (the `atu_method/` package, `tests/`, configuration files):
  MIT — see [LICENSE](LICENSE).
- **Documentation** (`docs/`, `memories/`, `scholarship/`, all Markdown
  outside the package): CC-BY-4.0 — see [LICENSE-DOCS](LICENSE-DOCS).

## Contact

`thebibleman77@gmail.com`
