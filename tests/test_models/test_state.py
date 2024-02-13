#!/usr/bin/python3
"""
This module contains unit tests for the State class.
"""

import os
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
from datetime import datetime
from time import sleep


class TestState(unittest.TestCase):
    """Defines the test cases for the State class."""

    def setUp(self):
        """Sets up the test environment."""
        self.state = State()

    def tearDown(self):
        """Tears down the test environment."""
        del self.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Tests if state is an instance of State and BaseModel."""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Tests if the State class has the correct attributes."""
        self.assertTrue("name" in self.state.__dir__())

    def test_save(self):
        """Tests the save method."""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method."""
        state_dict = self.state.to_dict()
        self.assertEqual(type(state_dict), dict)
        self.assertTrue('to_dict' in dir(self.state))

    def test_str(self):
        """Tests the __str__ method."""
        state_str = str(self.state)
        self.assertEqual(state_str, "[State] ({}) {}".format(self.state.id, self.state.__dict__))


if __name__ == "__main__":
    unittest.main()
