#!/usr/bin/python3
"""
This module contains unit tests for the User class.
"""

import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
from datetime import datetime
from time import sleep


class TestUser(unittest.TestCase):
    """Defines the test cases for the User class."""

    def setUp(self):
        """Sets up the test environment."""
        self.user = User()

    def tearDown(self):
        """Tears down the test environment."""
        del self.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Tests if user is an instance of User and BaseModel."""
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Tests if the User class has the correct attributes."""
        self.assertTrue("email" in self.user.__dir__())
        self.assertTrue("password" in self.user.__dir__())
        self.assertTrue("first_name" in self.user.__dir__())
        self.assertTrue("last_name" in self.user.__dir__())

    def test_save(self):
        """Tests the save method."""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method."""
        user_dict = self.user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertTrue('to_dict' in dir(self.user))

    def test_str(self):
        """Tests the __str__ method."""
        user_str = str(self.user)
        self.assertEqual(user_str, "[User] ({}) {}".format(self.user.id, self.user.__dict__))


if __name__ == "__main__":
    unittest.main()
