import math
import unittest

from tests.support import load_answer


class ShapesTests(unittest.TestCase):
    def test_hierarchy_and_polymorphism(self):
        module = load_answer("module_05", "shapes.py")
        circle = module.Circle("blue", 5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)
        self.assertEqual(circle.describe(), "A blue shape with area 78.54 and perimeter 31.42")
        self.assertEqual(module.Rectangle("green", 4, 6).perimeter(), 20)
        self.assertEqual(module.Triangle("yellow", 3, 4, 5).area(), 6)
        self.assertEqual(module.Square("purple", 5).area(), 25)
        shapes = [circle, module.Rectangle("green", 4, 6)]
        self.assertIs(module.largest_shape(shapes), circle)
        with self.assertRaises(NotImplementedError):
            module.Shape("red").area()


if __name__ == "__main__":
    unittest.main()
