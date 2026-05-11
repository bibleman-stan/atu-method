"""Validator-output infrastructure (universal).

Provides the Candidate dataclass + emit_candidate constructor + write_candidates
grouped-markdown report writer used by colometry/syntax validators in
per-corpus reader editions.

Per-project rule-name dictionaries are passed into write_candidates rather
than carried as a module-level constant, so the writer is generic across
corpora (BoFM rule labels, GNT rule labels, Tanakh rule labels, etc.).

Usage:
    from atu_method.infrastructure.validator_output import (
        Candidate, emit_candidate, write_candidates,
    )

    candidates = []
    candidates.append(emit_candidate(
        verse_ref="Matt 4:1",
        line_index=3,
        line_text="...",
        rule="R18",
        tag="STRONG-MERGE",
        error_class="DEVIATION",
        rationale="vocative-appositive merge",
    ))

    RULE_NAMES = {"R18": "vocative own line", ...}
    write_candidates(candidates, "report.md", title="Validator Report",
                     rule_names=RULE_NAMES)
"""

from __future__ import annotations

import os
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Mapping, Optional


@dataclass
class Candidate:
    """A validator finding flagged for editorial action."""
    verse_ref: str       # e.g. "Matt 4:1"
    line_index: int      # 0-based index within chapter
    line_text: str       # raw line content for context
    rule: str            # rule label, e.g. "R2", "R18", "M1"
    tag: str             # "STRONG-MERGE" | "STRONG-SPLIT" | "REVIEW-REQUIRED" | "AMBIG"
    error_class: str     # "MALFORMED" (Layer 1) | "DEVIATION" (Layer 3) | other
    rationale: str       # short description of why this is flagged
    context: str = ""    # optional surrounding lines


def emit_candidate(
    verse_ref: str,
    line_index: int,
    line_text: str,
    rule: str,
    tag: str,
    error_class: str,
    rationale: str,
    context: str = "",
) -> Candidate:
    """Constructor helper — same fields as Candidate dataclass."""
    return Candidate(verse_ref, line_index, line_text, rule, tag, error_class, rationale, context)


def write_candidates(
    candidates: list[Candidate],
    output_path: str,
    title: str = "Validator Report",
    rule_names: Optional[Mapping[str, str]] = None,
    class_order: Optional[list[str]] = None,
) -> None:
    """Write candidates as a grouped markdown report.

    Structure:
        # {title}

        ## MALFORMED (Layer 1 violations) — N total

        ### R18 — vocative own line (N)
        - verse_ref — line N — "text" — [tag] rationale

        ## DEVIATION (Layer 3 violations) — N total

        ### R19 — genitive absolute own line (N)
        - ...

    Args:
        candidates: list of Candidate (from emit_candidate or the dataclass).
        output_path: where to write the markdown file.
        title: top-level heading.
        rule_names: optional mapping {rule_code: human_readable_name} for
            "### RULE — name (N)" headers. If None, headers are bare rule codes.
        class_order: error-class ordering; default is ["MALFORMED", "DEVIATION"]
            with any other classes appended alphabetically.
    """
    rule_names = rule_names or {}
    class_order = class_order or ["MALFORMED", "DEVIATION"]

    by_class: dict[str, dict[str, list[Candidate]]] = defaultdict(lambda: defaultdict(list))
    for c in candidates:
        by_class[c.error_class][c.rule].append(c)

    remaining_classes = [k for k in sorted(by_class) if k not in class_order]
    all_classes = class_order + remaining_classes

    def rule_display(rule: str) -> str:
        name = rule_names.get(rule, "")
        return f"{rule} — {name}" if name else rule

    lines_out: list[str] = [f"# {title}", ""]

    for ec in all_classes:
        if ec not in by_class:
            continue
        ec_rules = by_class[ec]
        ec_total = sum(len(v) for v in ec_rules.values())
        lines_out.append(f"## {ec} — {ec_total} total")
        lines_out.append("")

        for rule in sorted(ec_rules.keys()):
            rule_candidates = ec_rules[rule]
            display = rule_display(rule)
            lines_out.append(f"### {display} ({len(rule_candidates)})")
            for c in rule_candidates:
                tag_str = f"[{c.tag}] " if c.tag else ""
                line_str = f'"{c.line_text}"' if c.line_text else "(empty)"
                lines_out.append(
                    f"- {c.verse_ref} — line {c.line_index} — {line_str} — "
                    f"{tag_str}{c.rationale}"
                )
                if c.context:
                    lines_out.append(f"  - context: {c.context}")
            lines_out.append("")

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines_out) + "\n")
