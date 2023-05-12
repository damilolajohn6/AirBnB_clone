#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
import os
from models.place import Place
from models import storage
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """Test Cases for the Place class."""

    def tearDown(self):
        """Tears down test methods."""
        self.reset_storage()

    def reset_storage(self):
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Place class."""
        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        place = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(place, k))
            self.assertEqual(type(getattr(place, k, None)), v)

if __name__ == "__main__":
    unittest.main()
