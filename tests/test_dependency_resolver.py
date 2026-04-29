import unittest

from practical_ds.dependency_resolver import resolve_dependencies


class DependencyResolverTests(unittest.TestCase):
    def test_orders_dependencies_before_dependents(self):
        order = resolve_dependencies(
            ["database", "api", "frontend", "docs"],
            {"api": ["database"], "frontend": ["api"]},
        )

        self.assertLess(order.index("database"), order.index("api"))
        self.assertLess(order.index("api"), order.index("frontend"))
        self.assertCountEqual(order, ["database", "api", "frontend", "docs"])

    def test_detects_cycles(self):
        with self.assertRaises(ValueError):
            resolve_dependencies(["a", "b"], {"a": ["b"], "b": ["a"]})

    def test_rejects_unknown_dependencies(self):
        with self.assertRaises(ValueError):
            resolve_dependencies(["a"], {"a": ["missing"]})


if __name__ == "__main__":
    unittest.main()

