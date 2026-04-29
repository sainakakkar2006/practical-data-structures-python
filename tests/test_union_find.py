import unittest

from practical_ds.union_find import UnionFind


class UnionFindTests(unittest.TestCase):
    def test_tracks_connected_components(self):
        groups = UnionFind(["alice", "bob", "carol"])

        self.assertFalse(groups.connected("alice", "bob"))
        self.assertTrue(groups.union("alice", "bob"))
        self.assertTrue(groups.connected("alice", "bob"))
        self.assertEqual(groups.group_size("alice"), 2)
        self.assertFalse(groups.connected("alice", "carol"))

    def test_union_returns_false_when_already_connected(self):
        groups = UnionFind(["a", "b"])
        groups.union("a", "b")

        self.assertFalse(groups.union("a", "b"))

    def test_rejects_unknown_items(self):
        groups = UnionFind(["a"])

        with self.assertRaises(KeyError):
            groups.find("missing")


if __name__ == "__main__":
    unittest.main()

