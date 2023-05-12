#!/usr/bin/python3
"""Unit test module for the City class."""

import unittest
import os
from models.city import City
from models.base_model import BaseModel
from models import storage


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.reset_storage()

    @staticmethod
    def resetStorage():
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of City class."""
        new_city = City()
        self.assertIsInstance(new_city, City)
        self.assertIsInstance(new_city, BaseModel)
        self.assertIs(type(new_city), City)

    def test_8_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        new_city = City()
        for key, value in attributes.items():
            self.assertTrue(hasattr(new_city, key))
            self.assertEqual(type(getattr(new_city, key)), value)


if __name__ == "__main__":
    unittest.main()
