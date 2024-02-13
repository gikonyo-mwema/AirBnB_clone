#!/usr/bin/python3
"""
This module contains unit tests for the Place class.
"""

import os
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage
from datetime import datetime
from time import sleep


class TestPlace(unittest.TestCase):
    """Defines the test cases for the Place class."""

    def setUp(self):
        """Sets up the test environment."""
        self.place = Place()

    def tearDown(self):
        """Tears down the test environment."""
        del self.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Tests if place is an instance of Place and BaseModel."""
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Tests if the Place class has the correct attributes."""
        self.assertTrue("city_id" in self.place.__dir__())
        self.assertTrue("user_id" in self.place.__dir__())
        self.assertTrue("name" in self.place.__dir__())
        self.assertTrue("description" in self.place.__dir__())
        self.assertTrue("number_rooms" in self.place.__dir__())
        self.assertTrue("number_bathrooms" in self.place.__dir__())
        self.assertTrue("max_guest" in self.place.__dir__())
        self.assertTrue("price_by_night" in self.place.__dir__())
        self.assertTrue("latitude" in self.place.__dir__())
        self.assertTrue("longitude" in self.place.__dir__())
        self.assertTrue("amenity_ids" in self.place.__dir__())

    def test_save(self):
        """Tests the save method."""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method."""
        place_dict = self.place.to_dict()
        self.assertEqual(type(place_dict), dict)
        self.assertTrue('to_dict' in dir(self.place))

    def test_str(self):
        """Tests the __str__ method."""
        place_str = str(self.place)
        self.assertEqual(place_str, "[Place] ({}) {}".format(self.place.id, self.place.__dict__))


if __name__ == "__main__":
    unittest.main()
