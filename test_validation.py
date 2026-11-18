import unittest

from validation import is_valid_bug_description


class TestBugDescriptionValidation(unittest.TestCase):

    def test_empty_description(self):
        self.assertFalse(is_valid_bug_description(""))

    def test_whitespace_only(self):
        self.assertFalse(is_valid_bug_description("   "))

    def test_valid_description(self):
        self.assertTrue(
            is_valid_bug_description("My C++ program crashes.")
        )

    def test_description_with_surrounding_spaces(self):
        self.assertTrue(
            is_valid_bug_description("  My Python script fails.  ")
        )

    def test_none_input(self):
        self.assertFalse(is_valid_bug_description(None))

    def test_numeric_input(self):
        self.assertFalse(is_valid_bug_description(12345))

    def test_newlines_and_tabs(self):
        self.assertFalse(is_valid_bug_description("\n\t  "))


if __name__ == "__main__":
    unittest.main()
