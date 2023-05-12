#!/usr/bin/python3
"""
Unit tests for file_storage module.
"""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class methods"""

    def test_instantiation(self):
        """Check that the class instantiates correctly"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docstrings(self):
        """Check that certain methods have docstrings"""
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

if __name__ == '__main__':
    unittest.main()
