#!/usr/bin/python3
"""
This module contains unit tests for the City class.
"""

import os
import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage
from datetime import datetime
from time import sleep


class TestCity(unittest.TestCase):
    """Defines the test cases for the City class."""

    def setUp(self):
        """Sets up the test environment."""
        self.city = City()

    def tearDown(self):
        """Tears down the test environment."""
        del self.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Tests if city is an instance of City and BaseModel."""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Tests if the City class has the correct attributes."""
        self.assertTrue("state_id" in self.city.__dir__())
        self.assertTrue("name" in self.city.__dir__())

    def test_save(self):
        """Tests the save method."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method."""
        city_dict = self.city.to_dict()
        self.assertEqual(type(city_dict), dict)
        self.assertTrue('to_dict' in dir(self.city))

    def test_str(self):
        """Tests the __str__ method."""
        city_str = str(self.city)
        self.assertEqual(city_str, "[City] ({}) {}".format(self.city.id, self.city.__dict__))


if __name__ == "__main__":
    unittest.main()
