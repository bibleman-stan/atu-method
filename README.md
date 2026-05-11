# ATU Method

> Computational colometry apparatus for revealing atomic thought units in
> canonical texts.

**Status:** Pre-release (0.1.0) — repository scaffold established; per-rule
scholarship companions and Python infrastructure extracted from the
proof-of-concept implementation in
[readers-bofm](https://github.com/bibleman-stan/readers-bofm). Extraction
is in progress; the package currently provides UD-parse query primitives
(`atu_method.parsing.conllu_query`, `atu_method.parsing.line_mapping`) and
transaction-logging infrastructure (`atu_method.infrastructure.tx_log`).
Additional planes (adapters, applier base classes, dashboard runner) will
follow as the BoFM apparatus stabilizes.

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

Pre-release; not yet on PyPI. The expected layout is **sibling-checkout**:
this repository lives alongside the per-corpus reader editions, and each
reader edition installs `atu-method` as an editable Python package into the
working environment.

```bash
# Clone alongside the reader edition(s) you intend to use.
cd ~/repos
git clone git@github.com:bibleman-stan/atu-method.git
git clone git@github.com:bibleman-stan/readers-bofm.git    # (e.g.)

# Install atu-method as editable -- one command, one time per env.
cd atu-method
python -m pip install -e .
```

After install, any Python process in the env can import the universal
primitives:

```python
from atu_method.parsing.conllu_query import load_conllu, Sentence, Token
from atu_method.parsing.line_mapping import build_line_map, build_line_map_full
from atu_method.infrastructure.tx_log import TxLog
```

Editable mode means edits to `atu_method/` source files are picked up
without reinstalling. Reader editions consume the package the same way; the
per-repo modules wrap the universal primitives with corpus-specific layout
glue (e.g., readers-bofm's `validators/parsing/line_mapping.py` adds a
`book_paths()` resolver for the BoFM's `data/text-files/v2-mine/` layout).

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

## Sibling-checkout convention

This repository is consumed by per-corpus reader editions via sibling
checkout, not via PyPI dependency resolution (until the package is
published). Documents and code reference each other using relative paths
like `../../atu-method/docs/framework.md` (from a reader edition into
this repo) and `readers-bofm/private/01-method/colometry-canon.md` (from
this repo into the BoFM reader edition).

Practical implication: cross-references resolve when both repositories are
cloned alongside each other under a shared parent directory. A one-repo
clone will see broken markdown links until the sibling is also cloned.

Validator/applier code in reader editions imports from `atu_method.*`
directly. Documentation cross-references rely on relative paths.

## Contact

`thebibleman77@gmail.com`
