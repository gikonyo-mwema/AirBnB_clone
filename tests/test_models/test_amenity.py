#!/usr/bin/python3
"""
This module contains unit tests for the Amenity class.
"""

import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
from datetime import datetime
from time import sleep


class TestAmenity(unittest.TestCase):
    """Defines the test cases for the Amenity class."""

    def setUp(self):
        """Sets up the test environment."""
        self.amenity = Amenity()

    def tearDown(self):
        """Tears down the test environment."""
        del self.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Tests if amenity is an instance of Amenity and BaseModel."""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Tests if the Amenity class has the correct attributes."""
        self.assertTrue("name" in self.amenity.__dir__())

    def test_save(self):
        """Tests the save method."""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method."""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(type(amenity_dict), dict)
        self.assertTrue('to_dict' in dir(self.amenity))

    def test_str(self):
        """Tests the __str__ method."""
        amenity_str = str(self.amenity)
        self.assertEqual(amenity_str, "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__))


if __name__ == "__main__":
    unittest.main()
