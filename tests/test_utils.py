import unittest
from src.utils import sanitize_user_input

class TestUtils(unittest.TestCase):
    def test_sanitize_user_input(self):
        # set up
        str = ("ITALIAN   OLIVE oil")
        # act
        sanitized_str = sanitize_user_input(str)
        expected_str = "italian olive oil"
        # assert
        self.assertEqual(sanitized_str, expected_str)

if __name__ == "__main__":
    unittest.main()