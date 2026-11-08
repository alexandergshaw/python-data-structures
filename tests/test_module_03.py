import unittest

from tests.support import load_answer


class CollectionsTests(unittest.TestCase):
    def test_student_helpers(self):
        module = load_answer("module_03", "collections.py")
        students = module.students
        self.assertEqual(len(students), 6)
        self.assertEqual(len(module.get_passing_students(students)), 4)
        self.assertEqual(module.get_average_grade([]), 0)
        self.assertEqual(module.count_by_major(students), {"CS": 3, "Math": 2, "Art": 1})
        self.assertEqual(module.get_top_student(students)["name"], "Alice")
        self.assertIsNone(module.get_top_student([]))
        self.assertEqual([s["name"] for s in module.filter_by_major(students, "CS")],
                         ["Alice", "Carol", "Frank"])


if __name__ == "__main__":
    unittest.main()
