from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar


K = TypeVar("K")
V = TypeVar("V")


@dataclass
class _Node(Generic[K, V]):
    key: K
    value: V
    prev: _Node[K, V] | None = None
    next: _Node[K, V] | None = None


class LRUCache(Generic[K, V]):
    """Fixed-size least-recently-used cache.

    A dictionary gives O(1) key lookup. A doubly linked list tracks usage order,
    so moving or evicting nodes is also O(1).
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._nodes: dict[K, _Node[K, V]] = {}
        self._head: _Node[K, V] | None = None
        self._tail: _Node[K, V] | None = None

    def get(self, key: K) -> V | None:
        node = self._nodes.get(key)
        if node is None:
            return None
        self._move_to_front(node)
        return node.value

    def put(self, key: K, value: V) -> None:
        node = self._nodes.get(key)
        if node is not None:
            node.value = value
            self._move_to_front(node)
            return

        node = _Node(key, value)
        self._nodes[key] = node
        self._add_to_front(node)

        if len(self._nodes) > self.capacity:
            self._evict_tail()

    def keys_most_recent_first(self) -> list[K]:
        keys: list[K] = []
        current = self._head
        while current is not None:
            keys.append(current.key)
            current = current.next
        return keys

    def __len__(self) -> int:
        return len(self._nodes)

    def _move_to_front(self, node: _Node[K, V]) -> None:
        if node is self._head:
            return
        self._remove(node)
        self._add_to_front(node)

    def _add_to_front(self, node: _Node[K, V]) -> None:
        node.prev = None
        node.next = self._head
        if self._head is not None:
            self._head.prev = node
        self._head = node
        if self._tail is None:
            self._tail = node

    def _remove(self, node: _Node[K, V]) -> None:
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self._head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self._tail = node.prev

        node.prev = None
        node.next = None

    def _evict_tail(self) -> None:
        if self._tail is None:
            return
        old_tail = self._tail
        self._remove(old_tail)
        del self._nodes[old_tail.key]

