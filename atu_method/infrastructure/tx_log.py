"""Transaction log for corpus appliers (universal).

Each apply session writes a JSON log of {file, line, action, before, after}
entries. A companion `rollback` mechanism reads the log and reverses entries
whose current state still matches the recorded `after`.

This module is the universal infrastructure piece. Per-corpus code provides
the per-repo TX_DIR location (e.g., `<repo>/validators/.tx/`).

Usage inside an applier::

    from atu_method.infrastructure.tx_log import TxLog

    tx = TxLog(
        rule_name="polysyndetic_verb_chain",
        tx_dir=Path("<repo>/validators/.tx"),
    )
    tx.record_split(str(v2_path), line_idx, original_line, left, right)
    tx.commit()   # writes <tx_dir>/<rule>_YYYYMMDD-HHMMSS.json
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


class TxLog:
    def __init__(self, rule_name: str, tx_dir: Path) -> None:
        """Initialise a transaction log.

        Args:
            rule_name: short slug used in the log filename.
            tx_dir: per-repo transaction-log directory (created if absent).
        """
        tx_dir = Path(tx_dir)
        tx_dir.mkdir(parents=True, exist_ok=True)
        self.rule_name = rule_name
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.path = tx_dir / f"{rule_name}_{ts}.json"
        self.entries: list[dict] = []

    def record_split(
        self,
        file: str,
        line_idx: int,
        before_text: str,
        after_left: str,
        after_right: str,
    ) -> None:
        """Record a split: one line -> two lines.

        line_idx is 0-based. after_left is the new content of line_idx;
        after_right is the newly-inserted line at line_idx+1.
        """
        self.entries.append(
            {
                "action": "split",
                "file": file,
                "line_idx": line_idx,
                "before": before_text,
                "after_left": after_left,
                "after_right": after_right,
            }
        )

    def record_merge(
        self,
        file: str,
        line_idx: int,
        before_a: str,
        before_b: str,
        after: str,
    ) -> None:
        """Record a merge: two lines -> one line.

        line_idx is 0-based; it is the line that absorbs the next.
        before_a is the original content of line_idx, before_b of line_idx+1;
        after is the merged content now at line_idx.
        """
        self.entries.append(
            {
                "action": "merge",
                "file": file,
                "line_idx": line_idx,
                "before_a": before_a,
                "before_b": before_b,
                "after": after,
            }
        )

    def commit(self) -> Path:
        """Write the log to disk. Returns the path written."""
        # Timestamp is the trailing YYYYMMDD-HHMMSS portion of the filename.
        stem = self.path.stem
        ts = stem[stem.rfind("_") + 1:]
        payload = {
            "rule": self.rule_name,
            "timestamp": ts,
            "entries": self.entries,
        }
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        return self.path

    def __len__(self) -> int:
        return len(self.entries)
