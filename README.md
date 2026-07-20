# Practical Data Structures in Python

**Name:** Saina Kakkar

## Design and Implementation

This repo is a collection of small data structure examples I made while
practicing core CS topics. I wanted the examples to feel more useful than
textbook code, so each one is connected to a normal software problem: caches
need fast lookup, autocomplete needs prefix search, task queues need
priorities, dependency planners need graph traversal, and connected groups
can be handled with union-find.

## Files

| File | Data Structure | Example Use |
| --- | --- | --- |
| `lru_cache.py` | dictionary + doubly linked list | keeping recently used values |
| `dependency_resolver.py` | graph | ordering tasks with prerequisites |
| `autocomplete.py` | trie | finding words from a prefix |
| `priority_task_queue.py` | heap | picking the most important task first |
| `union_find.py` | disjoint set | checking which items are connected |

## Run

Run the demo:

```bash
PYTHONPATH=src python examples/demo.py
```

## Verify

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

If every test passes, each structure behaves the way its real-world use case
needs it to.

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
Note that the `get("user:1")` call in the middle is what saves `user:1`.
Reading an item counts as using it, not only writing. That detail is easy to
get wrong in an LRU implementation, which is why the tests check it.

## Notes

I wanted a GitHub project that shows I understand data structures, but in a
way that is still practical. Writing tests for each structure ended up being
the most useful part. Thinking about time complexity is one thing, but
proving the eviction order of an LRU cache with a test is what made the
behavior stick for me. Could've stopped at the classes themselves, but I
added the demo script and per-structure tests so the repo is easy for
someone else to run and poke at.
