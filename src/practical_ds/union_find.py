from __future__ import annotations

from collections.abc import Hashable


class UnionFind:
    """Track connected groups with path compression and union by size."""

    def __init__(self, items: list[Hashable]):
        unique_items = list(dict.fromkeys(items))
        self._parent = {item: item for item in unique_items}
        self._size = {item: 1 for item in unique_items}

    def find(self, item: Hashable) -> Hashable:
        if item not in self._parent:
            raise KeyError(f"unknown item: {item}")

        root = item
        while self._parent[root] != root:
            root = self._parent[root]

        while self._parent[item] != item:
            parent = self._parent[item]
            self._parent[item] = root
            item = parent

        return root

    def union(self, left: Hashable, right: Hashable) -> bool:
        left_root = self.find(left)
        right_root = self.find(right)

        if left_root == right_root:
            return False

        if self._size[left_root] < self._size[right_root]:
            left_root, right_root = right_root, left_root

        self._parent[right_root] = left_root
        self._size[left_root] += self._size[right_root]
        return True

    def connected(self, left: Hashable, right: Hashable) -> bool:
        return self.find(left) == self.find(right)

    def group_size(self, item: Hashable) -> int:
        return self._size[self.find(item)]

