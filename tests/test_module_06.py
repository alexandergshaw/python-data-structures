import unittest

from tests.support import load_answer


class LinkedListTests(unittest.TestCase):
    def test_mutations_search_length_reverse_and_empty(self):
        module = load_answer("module_06", "linked_list.py")
        values = module.LinkedList()
        self.assertEqual(str(values), "None")
        for value in [10, 20, 30]:
            values.append(value)
        values.prepend(5)
        values.delete(20)
        self.assertEqual(str(values), "5 → 10 → 30 → None")
        self.assertTrue(values.search(10))
        self.assertFalse(values.search(99))
        self.assertEqual(values.length(), 3)
        values.reverse()
        self.assertEqual(str(values), "30 → 10 → 5 → None")
        for value in [30, 10, 5, 5]:
            values.delete(value)
        self.assertEqual(values.length(), 0)
        self.assertEqual(str(values), "None")


if __name__ == "__main__":
    unittest.main()
