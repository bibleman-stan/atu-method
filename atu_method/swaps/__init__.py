"""Swap system — universal archaic-word modernization for KJV-style corpora.

Provides HTML span-wrapped swap markup identical to bomreader's deployed
swap system. The UX is corpus-agnostic; only the swap-list data varies
per corpus (NT archaisms differ from OT archaisms).

Exports:
    apply_swaps   — wraps archaic tokens in <span class="swap"> markup
    load_corpus_swap_list — loads + merges universal + corpus-specific lists
"""

from .apply_swaps import apply_swaps
from .load_lists import load_corpus_swap_list

__all__ = ["apply_swaps", "load_corpus_swap_list"]
