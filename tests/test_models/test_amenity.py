#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import os
import unittest
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods.
        deletes any test objects during test methods"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tears down test methods. deletes
        any tets objects during tests methods"""
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data.
        resets __ dictionary and deletes JSON file"""
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)


    def test_instantiation(self):
         """Tests instantiation of Amenity class.
          tests if self.amenity is an instance of the Amenity class, tests if it's a subclass of BaseModel"""
         self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Amenity class.
        tests if the name attribute exists and is a string"""

        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(type(getattr(self.amenity, "name", None)), str)

if __name__ == "__main__":
    unittest.main()
