#!/usr/bin/python3

"""Unittest module for the State Class."""

import unittest
import os
from models import storage
from models.state import State
from models.engine.file_storage import FileStorage

class TestState(unittest.TestCase):

    """Test Cases for the State class."""

    def tearDown(self):
        """Tears down test methods."""
        self.reset_storage()
        pass

    def reset_storage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of State class."""
        state_instance = State()
        self.assertEqual(str(type(state_instance)), "<class 'models.state.State'>")
        self.assertIsInstance(state_instance, State)
        self.assertTrue(issubclass(type(state_instance), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of State class."""
        attributes = storage.attributes()["State"]
        state_instance = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(state_instance, k))
            self.assertEqual(type(getattr(state_instance, k, None)), v)

if __name__ == "__main__":
    unittest.main()
