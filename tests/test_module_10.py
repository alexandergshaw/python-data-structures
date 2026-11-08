import unittest

from tests.support import load_answer


class BSTTests(unittest.TestCase):
    def test_operations_and_deletion(self):
        module = load_answer("module_10", "bst.py")
        tree = module.BinarySearchTree()
        for value in [8, 3, 10, 1, 6, 14, 4, 7]:
            tree.insert(value)
        self.assertEqual(tree.inorder(), [1, 3, 4, 6, 7, 8, 10, 14])
        self.assertEqual(tree.preorder(), [8, 3, 1, 6, 4, 7, 10, 14])
        self.assertEqual(tree.postorder(), [1, 4, 7, 6, 3, 14, 10, 8])
        self.assertEqual(tree.level_order(), [8, 3, 10, 1, 6, 14, 4, 7])
        self.assertTrue(tree.search(6))
        self.assertFalse(tree.search(5))
        self.assertEqual((tree.height(), tree.minimum(), tree.maximum()), (3, 1, 14))
        tree.delete(3)
        tree.delete(8)
        self.assertEqual(tree.inorder(), [1, 4, 6, 7, 10, 14])
        empty = module.BinarySearchTree()
        self.assertEqual(empty.height(), -1)
        with self.assertRaises(ValueError):
            empty.minimum()


if __name__ == "__main__":
    unittest.main()
