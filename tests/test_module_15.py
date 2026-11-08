import unittest

from tests.support import load_answer


class DynamicProgrammingTests(unittest.TestCase):
    def test_dynamic_programming_functions(self):
        module = load_answer("module_15", "dynamic_programming.py")
        self.assertEqual(module.fib_memo(50), 12586269025)
        self.assertEqual(module.fib_memo(30), module.fib_tab(30))
        self.assertEqual(module.coin_change([10, 6, 1], 12), 2)
        self.assertEqual(module.coin_change([2], 3), -1)
        self.assertEqual(module.climb_stairs(10), 89)
        self.assertEqual(module.lcs("ABCBDAB", "BDCAB"), 4)
        sequence = module.lcs_sequence("ABCBDAB", "BDCAB")
        self.assertIn(sequence, ("BCAB", "BDAB"))
        self.assertEqual(module.knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7), 9)
        self.assertEqual(module.knapsack([], [], 10), 0)


if __name__ == "__main__":
    unittest.main()
