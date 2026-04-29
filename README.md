# Practical Data Structures in Python

A small portfolio repo showing core data structures through practical software-development examples. Each module includes readable code, tests, and a short explanation of when the data structure is useful.

## Why This Project Exists

Data structures are not only interview topics. They show up in real systems:

- caches need fast lookup and eviction
- dependency tools need graph traversal
- search boxes need prefix lookup
- schedulers need priority queues
- network/grouping problems need disjoint sets

This repo turns those ideas into small, testable Python implementations.

## Projects

| Module | Data Structure | Practical Use Case |
| --- | --- | --- |
| `lru_cache.py` | Hash map + doubly linked list | Keep most recently used values and evict old ones |
| `dependency_resolver.py` | Directed graph + topological sort | Order tasks/packages based on dependencies |
| `autocomplete.py` | Trie | Return suggestions by prefix |
| `priority_task_queue.py` | Heap | Schedule highest-priority tasks first |
| `union_find.py` | Disjoint set union | Track connected groups efficiently |

## Quick Start

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

Run a small demo:

```bash
python examples/demo.py
```

## Example

```python
from practical_ds.lru_cache import LRUCache

cache = LRUCache(capacity=2)
cache.put("user:1", "Saina")
cache.put("user:2", "Ari")
cache.get("user:1")
cache.put("user:3", "Mina")

assert cache.get("user:2") is None
```

## What This Shows

This repo is designed to show that I understand data structures, can connect them to real software problems, and can write clean, tested Python code.
