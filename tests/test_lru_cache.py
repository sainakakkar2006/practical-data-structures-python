import unittest

from practical_ds.lru_cache import LRUCache


class LRUCacheTests(unittest.TestCase):
    def test_evicts_least_recently_used_key(self):
        cache = LRUCache[str, int](capacity=2)
        cache.put("a", 1)
        cache.put("b", 2)
        self.assertEqual(cache.get("a"), 1)
        cache.put("c", 3)

        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.keys_most_recent_first(), ["c", "a"])

    def test_updates_existing_key(self):
        cache = LRUCache[str, int](capacity=2)
        cache.put("a", 1)
        cache.put("a", 10)

        self.assertEqual(cache.get("a"), 10)
        self.assertEqual(len(cache), 1)

    def test_requires_positive_capacity(self):
        with self.assertRaises(ValueError):
            LRUCache(capacity=0)


if __name__ == "__main__":
    unittest.main()

