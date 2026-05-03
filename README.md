# Practical Data Structures in Python

This repo is a collection of small data structure examples I made while practicing core CS topics.

I wanted the examples to feel more useful than just textbook code, so each one is connected to a normal software problem.

## What's Inside

| File | Data Structure | Example Use |
| --- | --- | --- |
| `lru_cache.py` | dictionary + doubly linked list | keeping recently used values |
| `dependency_resolver.py` | graph | ordering tasks with prerequisites |
| `autocomplete.py` | trie | finding words from a prefix |
| `priority_task_queue.py` | heap | picking the most important task first |
| `union_find.py` | disjoint set | checking which items are connected |

## Why I Made This

I wanted a GitHub project that shows I understand data structures, but in a way that is still practical.

For example:

- caches need fast lookup
- autocomplete needs prefix search
- task queues need priorities
- dependency planners need graph traversal
- connected groups can be handled with union-find

## Quick Start

Run the tests:

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

Run the demo:

```bash
PYTHONPATH=src python examples/demo.py
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

Here, `user:2` gets removed because it was the least recently used item.

## What I Practiced

- writing clean Python classes
- using tests to check behavior
- thinking about time complexity
- connecting data structures to real examples
- making a repo that is easy to run

