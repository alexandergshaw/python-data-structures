import unittest

from tests.support import load_answer


class SearchSortTests(unittest.TestCase):
    def test_search_and_all_sorts(self):
        module = load_answer("module_09", "searching_sorting.py")
        values = [5, 3, 8, 1, 3]
        original = values[:]
        self.assertEqual(module.linear_search(values, 3), 1)
        self.assertEqual(module.linear_search(values, 9), -1)
        self.assertEqual(module.binary_search([1, 3, 5, 8], 5), 2)
        self.assertEqual(module.binary_search([1, 3, 5, 8], 4), -1)
        self.assertEqual(module.merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        for sorter in [module.bubble_sort, module.selection_sort, module.merge_sort, module.quick_sort]:
            self.assertEqual(sorter(values), sorted(values))
            self.assertEqual(values, original)


if __name__ == "__main__":
    unittest.main()
