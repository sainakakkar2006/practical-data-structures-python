from practical_ds import (
    AutocompleteIndex,
    LRUCache,
    PriorityTaskQueue,
    UnionFind,
    resolve_dependencies,
)


def main() -> None:
    cache = LRUCache[str, str](capacity=2)
    cache.put("profile:1", "Saina")
    cache.put("profile:2", "Ari")
    cache.get("profile:1")
    cache.put("profile:3", "Mina")
    print("Cache keys:", cache.keys_most_recent_first())

    order = resolve_dependencies(
        ["database", "api", "frontend"],
        {"api": ["database"], "frontend": ["api"]},
    )
    print("Build order:", order)

    autocomplete = AutocompleteIndex(["array", "argument", "graph", "greedy"])
    print("Suggestions for 'ar':", autocomplete.suggest("ar"))

    tasks = PriorityTaskQueue()
    tasks.add("fix login bug", priority=1)
    tasks.add("update docs", priority=3)
    print("Next task:", tasks.pop_next())

    network = UnionFind(["alice", "bob", "carol"])
    network.union("alice", "bob")
    print("Alice connected to Bob:", network.connected("alice", "bob"))


if __name__ == "__main__":
    main()

