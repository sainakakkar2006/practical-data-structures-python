from __future__ import annotations

from collections import defaultdict, deque
from collections.abc import Iterable


def resolve_dependencies(items: Iterable[str], dependencies: dict[str, list[str]]) -> list[str]:
    """Return an order where every dependency appears before the item that needs it."""

    all_items = list(dict.fromkeys(items))
    known = set(all_items)
    indegree = {item: 0 for item in all_items}
    outgoing: dict[str, list[str]] = defaultdict(list)

    for item, deps in dependencies.items():
        if item not in known:
            raise ValueError(f"unknown item in dependency map: {item}")

        for dependency in deps:
            if dependency not in known:
                raise ValueError(f"unknown dependency: {dependency}")
            outgoing[dependency].append(item)
            indegree[item] += 1

    ready = deque(item for item in all_items if indegree[item] == 0)
    ordered: list[str] = []

    while ready:
        current = ready.popleft()
        ordered.append(current)

        for neighbor in outgoing[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                ready.append(neighbor)

    if len(ordered) != len(all_items):
        raise ValueError("dependency cycle detected")

    return ordered

