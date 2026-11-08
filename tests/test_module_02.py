import contextlib
import io
import unittest
from unittest.mock import patch

from tests.support import load_answer


class ControlFlowTests(unittest.TestCase):
    def test_validation_skip_early_exit_and_report(self):
        module = load_answer("module_02", "control_flow.py")
        output = io.StringIO()
        with patch("builtins.input", side_effect=["4", "-1", "150", "85", "999"]):
            with contextlib.redirect_stdout(output):
                module.main()
        text = output.getvalue()
        self.assertIn("Skipping student 1", text)
        self.assertIn("Early exit triggered.", text)
        self.assertIn("Student 1: 85 → B", text)
        self.assertIn("Average: 85.00", text)

    def test_student_count_is_reprompted(self):
        module = load_answer("module_02", "control_flow.py")
        with patch("builtins.input", side_effect=["0", "1", "75"]):
            self.assertEqual(module.collect_scores(), [75])

    def test_empty_statistics_are_skipped(self):
        module = load_answer("module_02", "control_flow.py")
        with patch("builtins.input", side_effect=["1", "999"]):
            self.assertEqual(module.collect_scores(), [])


if __name__ == "__main__":
    unittest.main()
