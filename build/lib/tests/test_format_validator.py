# tests/test_format_validator.py

import unittest
from flatwhite import validate_format

class TestFormatValidator(unittest.TestCase):
    def test_validate_format(self):
        self.assertTrue(validate_format("some data"))

if __name__ == '__main__':
    unittest.main()
