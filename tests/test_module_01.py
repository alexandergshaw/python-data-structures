import contextlib
import io
import unittest
from unittest.mock import patch

from tests.support import load_answer


class BasicsTests(unittest.TestCase):
    def test_profile_and_gpa_status(self):
        module = load_answer("module_01", "basics.py")
        for gpa, status in [(3.5, "Excellent"), (3.0, "Good"), (2.0, "Satisfactory"), (1.9, "Needs improvement")]:
            output = io.StringIO()
            with patch("builtins.input", side_effect=["Alex", "20", str(gpa)]):
                with contextlib.redirect_stdout(output):
                    module.main()
            self.assertIn("Approximate birth year: 2006", output.getvalue())
            self.assertIn(f"GPA: {gpa:.2f}", output.getvalue())
            self.assertIn(f"GPA status: {status}", output.getvalue())


if __name__ == "__main__":
    unittest.main()
