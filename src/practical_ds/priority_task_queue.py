from __future__ import annotations

import heapq
from dataclasses import dataclass, field


@dataclass(order=True)
class _PrioritizedTask:
    priority: int
    insertion_order: int
    name: str = field(compare=False)


class PriorityTaskQueue:
    """Priority queue where lower priority numbers are handled first."""

    def __init__(self):
        self._heap: list[_PrioritizedTask] = []
        self._counter = 0

    def add(self, name: str, priority: int) -> None:
        if not name.strip():
            raise ValueError("task name is required")
        heapq.heappush(self._heap, _PrioritizedTask(priority, self._counter, name))
        self._counter += 1

    def pop_next(self) -> str:
        if not self._heap:
            raise IndexError("cannot pop from an empty queue")
        return heapq.heappop(self._heap).name

    def peek(self) -> str:
        if not self._heap:
            raise IndexError("cannot peek into an empty queue")
        return self._heap[0].name

    def __len__(self) -> int:
        return len(self._heap)

