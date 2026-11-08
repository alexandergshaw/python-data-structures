import contextlib
import io
import unittest
from unittest.mock import patch

from tests.support import load_answer


class CapstoneTests(unittest.TestCase):
    def test_text_analysis_helpers(self):
        module = load_answer("module_16", "main.py")
        text = "Python, python! Data."
        self.assertEqual(module.tokenize(text), ["python", "python", "data"])
        self.assertEqual(module.word_frequencies(text), {"python": 2, "data": 1})
        words = sorted(["data", "python"])
        self.assertEqual(module.binary_search(words, "python"), 1)
        self.assertEqual(module.binary_search(words, "missing"), -1)
        self.assertEqual(module.lcs_length(["a", "b", "c"], ["b", "c"]), 2)
        self.assertEqual(module.readability(module.tokenize(text), text)["average words per sentence"], 1.5)

    def test_demo_outputs_report_and_handles_missing_search(self):
        module = load_answer("module_16", "main.py")
        output = io.StringIO()
        with patch("builtins.input", return_value="notaword"), contextlib.redirect_stdout(output):
            module.analyze("A short text.", "A short example.")
        self.assertIn("not found", output.getvalue())
        self.assertIn("LCS length:", output.getvalue())
        self.assertIn("Readability:", output.getvalue())


if __name__ == "__main__":
    unittest.main()
