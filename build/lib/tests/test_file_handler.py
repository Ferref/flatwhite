# tests/test_file_handler.py

import unittest
from flatwhite import handle_file

class TestFileHandler(unittest.TestCase):
    def test_handle_file(self):
        self.assertTrue(handle_file("path/to/file"))

if __name__ == '__main__':
    unittest.main()
