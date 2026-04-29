import unittest

from practical_ds.priority_task_queue import PriorityTaskQueue


class PriorityTaskQueueTests(unittest.TestCase):
    def test_pops_tasks_by_priority_then_insertion_order(self):
        queue = PriorityTaskQueue()
        queue.add("medium", priority=2)
        queue.add("urgent first", priority=1)
        queue.add("urgent second", priority=1)

        self.assertEqual(queue.pop_next(), "urgent first")
        self.assertEqual(queue.pop_next(), "urgent second")
        self.assertEqual(queue.pop_next(), "medium")

    def test_peek_does_not_remove_task(self):
        queue = PriorityTaskQueue()
        queue.add("task", priority=5)

        self.assertEqual(queue.peek(), "task")
        self.assertEqual(len(queue), 1)

    def test_empty_queue_errors(self):
        queue = PriorityTaskQueue()

        with self.assertRaises(IndexError):
            queue.pop_next()


if __name__ == "__main__":
    unittest.main()

