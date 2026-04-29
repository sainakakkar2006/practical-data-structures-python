"""Practical data structure implementations."""

from .autocomplete import AutocompleteIndex
from .dependency_resolver import resolve_dependencies
from .lru_cache import LRUCache
from .priority_task_queue import PriorityTaskQueue
from .union_find import UnionFind

__all__ = [
    "AutocompleteIndex",
    "LRUCache",
    "PriorityTaskQueue",
    "UnionFind",
    "resolve_dependencies",
]

