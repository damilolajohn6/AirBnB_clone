#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.reset_storage()
        pass

    def reset_storage(self):
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of User class."""
        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        o = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
