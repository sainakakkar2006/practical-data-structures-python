from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class _TrieNode:
    children: dict[str, _TrieNode] = field(default_factory=dict)
    word: str | None = None


class AutocompleteIndex:
    """Prefix search built with a trie."""

    def __init__(self, words: list[str] | None = None):
        self._root = _TrieNode()
        for word in words or []:
            self.add(word)

    def add(self, word: str) -> None:
        cleaned = word.strip().lower()
        if not cleaned:
            return

        node = self._root
        for char in cleaned:
            node = node.children.setdefault(char, _TrieNode())
        node.word = cleaned

    def suggest(self, prefix: str, *, limit: int = 5) -> list[str]:
        if limit <= 0:
            raise ValueError("limit must be positive")

        node = self._root
        cleaned = prefix.strip().lower()
        for char in cleaned:
            if char not in node.children:
                return []
            node = node.children[char]

        suggestions: list[str] = []
        self._collect(node, suggestions, limit)
        return suggestions

    def _collect(self, node: _TrieNode, suggestions: list[str], limit: int) -> None:
        if len(suggestions) >= limit:
            return

        if node.word is not None:
            suggestions.append(node.word)

        for char in sorted(node.children):
            self._collect(node.children[char], suggestions, limit)

