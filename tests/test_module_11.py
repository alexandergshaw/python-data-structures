import unittest

from tests.support import load_answer


class HeapTests(unittest.TestCase):
    def test_heap_priority_queue_and_empty_errors(self):
        module = load_answer("module_11", "heap.py")
        heap = module.MinHeap()
        with self.assertRaises(IndexError):
            heap.peek()
        values = [9, 4, 7, 1, 8, 3, 6, 2, 5]
        for value in values:
            heap.push(value)
        self.assertEqual([heap.pop() for _ in values], sorted(values))
        with self.assertRaises(IndexError):
            heap.pop()
        queue = module.PriorityQueue()
        queue.push(1, "first")
        queue.push(1, "second")
        queue.push(3, "last")
        self.assertEqual([queue.pop(), queue.pop(), queue.pop()], ["first", "second", "last"])


if __name__ == "__main__":
    unittest.main()
