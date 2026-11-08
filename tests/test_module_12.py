import unittest

from tests.support import load_answer


class HashTableTests(unittest.TestCase):
    def test_chaining_and_tombstones(self):
        module = load_answer("module_12", "hash_table.py")
        chain = module.HashTableChaining(size=8)
        probing = module.HashTableProbing(size=8)
        colliding = {}
        for key in (f"key-{i}" for i in range(100)):
            colliding.setdefault(hash(key) % 8, []).append(key)
        first, second = next(keys[:2] for keys in colliding.values() if len(keys) >= 2)
        for table in (chain, probing):
            table.put(first, 1)
            table.put(second, 2)
            self.assertEqual(table.get(second), 2)
            table.delete(first)
            self.assertEqual(table.get(second), 2)
            with self.assertRaises(KeyError):
                table.get(first)
        chain.put(second, 3)
        self.assertEqual(chain.get(second), 3)
        self.assertEqual(chain.count, 1)
        self.assertEqual(chain.load_factor(), 1 / 8)


if __name__ == "__main__":
    unittest.main()
