import unittest

from tests.support import load_answer


class ParadigmTests(unittest.TestCase):
    def test_greedy_and_kadane(self):
        module = load_answer("module_14", "paradigms.py")
        activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
        self.assertEqual(module.activity_selection(activities), [(1, 4), (5, 7), (8, 11)])
        self.assertEqual(module.coin_change_greedy([25, 10, 5, 1], 41), [25, 10, 5, 1])
        self.assertEqual(module.coin_change_greedy([10, 6, 1], 12), [10, 1, 1])
        values = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(module.max_subarray_kadane(values), 6)
        total, start, end = module.max_subarray_indices(values)
        self.assertEqual((total, values[start:end + 1]), (6, [4, -1, 2, 1]))
        self.assertEqual(module.max_subarray_kadane([-3, -1, -4]), -1)


if __name__ == "__main__":
    unittest.main()
