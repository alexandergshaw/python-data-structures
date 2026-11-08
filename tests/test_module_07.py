import unittest

from tests.support import load_answer


class StackQueueTests(unittest.TestCase):
    def test_stack_queue_and_brackets(self):
        module = load_answer("module_07", "stacks_queues.py")
        stack = module.Stack()
        with self.assertRaises(IndexError):
            stack.pop()
        for value in [1, 2, 3]:
            stack.push(value)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.size(), 2)
        queue = module.Queue()
        for value in ["Alice", "Bob"]:
            queue.enqueue(value)
        self.assertEqual(queue.dequeue(), "Alice")
        self.assertEqual(queue.front(), "Bob")
        with self.assertRaises(IndexError):
            module.Queue().dequeue()
        for text, expected in [("({[]})", True), ("{[()]}", True), ("({[})", False),
                               ("((())", False), ("hello()[]", True), ("", True)]:
            self.assertEqual(module.is_balanced(text), expected)

    def test_undo_redo_and_branch_clears_redo(self):
        module = load_answer("module_07", "stacks_queues.py")
        undo, redo = module.Stack(), module.Stack()
        module.do_action("type", undo, redo)
        self.assertEqual(module.undo(undo, redo), "type")
        self.assertEqual(module.redo(undo, redo), "type")
        module.undo(undo, redo)
        module.do_action("new", undo, redo)
        self.assertIsNone(module.redo(undo, redo))


if __name__ == "__main__":
    unittest.main()
