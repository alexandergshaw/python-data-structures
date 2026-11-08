import unittest

from tests.support import load_answer


class ComplexityTests(unittest.TestCase):
    def test_search_duplicate_and_pair_functions(self):
        module = load_answer("module_04", "complexity.py")
        self.assertEqual(module.find_first([1, 2, 2], 2), 1)
        self.assertEqual(module.find_first([], 4), -1)
        for values, expected in [([1, 2, 3], False), ([1, 2, 1], True)]:
            self.assertEqual(module.has_duplicates_slow(values), expected)
            self.assertEqual(module.has_duplicates_fast(values), expected)
        self.assertEqual(module.binary_search([1, 3, 5], 3), 1)
        self.assertEqual(module.binary_search([1, 3, 5], 4), -1)
        self.assertEqual(module.sum_pairs([-3, 1, 3, -1, 2]), [(-3, 3), (1, -1)])


if __name__ == "__main__":
    unittest.main()
