#!/usr/bin/python3
""" Define unittest for user"""

import os
import models
from models.user import User

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the User class."""

    def setUp(self):
        """Set up the test case."""
        self.user = User()

    def test_init(self):
        """Test the __init__ method."""
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        """Test the to_dict method."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last_name)

    # Add more tests as needed...


if __name__ == '__main__':
    unittest.main()
