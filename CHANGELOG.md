# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] — 2026-05-10

### Added

- Initial repository scaffold.
- MIT license for code (`LICENSE`).
- CC-BY-4.0 license for documentation (`LICENSE-DOCS`).
- `CITATION.cff` for machine-readable scholarly citation.
- `pyproject.toml` configuring the `atu_method` Python package with
  hatchling backend.
- Stub Python package structure: `atu_method/{parsing,adapters,infrastructure,hooks,english}/`.
- Documentation scaffold: `docs/{architecture,apparatus,framework,glossary,rule-template,change-protocol}.md`.
- Memories scaffold: `memories/_index.md` for cross-project discipline lessons.
- Scholarship scaffold: `scholarship/_index.md` for per-rule rationale companions.
- This changelog.

### Status

This release establishes the repository and licensing structure. Substantive
content (Python infrastructure, framework documentation, discipline memories,
rule-template specification) will be extracted in subsequent releases from
the proof-of-concept implementation in
[readers-bofm](https://github.com/bibleman-stan/readers-bofm).
