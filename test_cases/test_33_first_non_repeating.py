import os
import sys
import unittest
import importlib.util

file_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        'codes',
        '33_first_non_repeating.py'
    )
)

spec = importlib.util.spec_from_file_location(
    "first_non_repeating",
    file_path
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

first_non_repeating_char = module.first_non_repeating_char


class TestFirstNonRepeatingChar(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            first_non_repeating_char("swiss"), "w"
        )

    def test_all_repeating(self):
        self.assertEqual(
            first_non_repeating_char("aabbcc"), None
        )

    def test_empty_string(self):
        self.assertEqual(
            first_non_repeating_char(""), None
        )

    def test_single_char(self):
        self.assertEqual(
            first_non_repeating_char("a"), "a"
        )


if __name__ == "__main__":
    unittest.main()