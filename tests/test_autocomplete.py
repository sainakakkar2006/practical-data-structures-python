import unittest

from practical_ds.autocomplete import AutocompleteIndex


class AutocompleteTests(unittest.TestCase):
    def test_suggests_words_by_prefix(self):
        index = AutocompleteIndex(["array", "argument", "graph", "greedy"])

        self.assertEqual(index.suggest("ar"), ["argument", "array"])
        self.assertEqual(index.suggest("g"), ["graph", "greedy"])

    def test_respects_limit(self):
        index = AutocompleteIndex(["apple", "app", "apply"])

        self.assertEqual(index.suggest("app", limit=2), ["app", "apple"])

    def test_requires_positive_limit(self):
        index = AutocompleteIndex(["array"])

        with self.assertRaises(ValueError):
            index.suggest("a", limit=0)


if __name__ == "__main__":
    unittest.main()

