import unittest

from tests.support import load_answer


class RecursionTests(unittest.TestCase):
    def test_recursive_functions(self):
        module = load_answer("module_08", "recursion.py")
        self.assertEqual(module.factorial(0), 1)
        self.assertEqual(module.factorial(5), 120)
        self.assertEqual(module.fibonacci(7), 13)
        self.assertEqual(module.recursive_sum([]), 0)
        self.assertEqual(module.recursive_sum([10, -3, 7]), 14)
        self.assertEqual(module.reverse_string("Python"), "nohtyP")
        self.assertEqual(module.power(3, 4), 81)
        self.assertEqual(module.count_occurrences([1, 2, 2, 2], 2), 3)
        self.assertEqual(module.flatten([1, [2, [3, [4]]]]), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
