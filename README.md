# practical-data-structures-python

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

## What Each One Provides

**`LRUCache(capacity)`** with `get(key)`, `put(key, value)`,
`keys_most_recent_first()`, and `len()`. The dictionary gives O(1) lookup
and the doubly linked list gives O(1) reordering, which is the whole point
of the combination. Using either one alone makes some operation linear.

**`resolve_dependencies(items, dependencies)`** takes a list of items and a
dict of prerequisites and returns a valid order, so `{"deploy": ["build",
"test"]}` guarantees `build` and `test` come before `deploy`. This is
topological sorting applied to an everyday problem.

**`AutocompleteIndex(words)`** with `add(word)` and
`suggest(prefix, limit=5)`. The trie means suggesting completions for a
prefix does not require scanning every word, only walking down the prefix
and collecting below it.

**`PriorityTaskQueue()`** with `add(name, priority)`, `pop_next()`, and
`peek()`. A heap keeps the most important task reachable in O(log n) time
without re-sorting the whole queue on every insert.

**`UnionFind(items)`** with `union(a, b)`, `find(item)`,
`connected(a, b)`, and `group_size(item)`. It answers "are these two things
in the same group" almost instantly even after many merges.

## Run

Run the demo:

```bash
PYTHONPATH=src python examples/demo.py
```

## Verify

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

There is one test file per structure. If every test passes, each structure
behaves the way its real-world use case needs it to.

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
behavior stick for me. I added the demo script and per-structure tests so
the repo is easy for someone else to run and poke at.

## License

MIT. See the [LICENSE](LICENSE) file.
