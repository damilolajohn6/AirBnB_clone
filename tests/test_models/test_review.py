#!/usr/bin/python3

"""Unittest module for the Review Class."""

import os
import re
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
from models import storage

class TestReview(unittest.TestCase):
    """Test Cases for the Review class."""

    def setUp(self):
        """Sets up test methods."""
        self.reset_storage()

    def tearDown(self):
        """Tears down test methods."""
        self.reset_storage()

    def reset_storage(self):
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Review class."""
        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Review class."""
        attributes = storage.classes["Review"].__dict__["__init__"].__annotations__
        o = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
