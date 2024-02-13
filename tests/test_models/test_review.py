#!/usr/bin/python3
"""
This module contains unit tests for the Review class.
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage
from datetime import datetime
from time import sleep


class TestReview(unittest.TestCase):
    """Defines the test cases for the Review class."""

    def setUp(self):
        """Sets up the test environment."""
        self.review = Review()

    def tearDown(self):
        """Tears down the test environment."""
        del self.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Tests if review is an instance of Review and BaseModel."""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Tests if the Review class has the correct attributes."""
        self.assertTrue("place_id" in self.review.__dir__())
        self.assertTrue("user_id" in self.review.__dir__())
        self.assertTrue("text" in self.review.__dir__())

    def test_save(self):
        """Tests the save method."""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method."""
        review_dict = self.review.to_dict()
        self.assertEqual(type(review_dict), dict)
        self.assertTrue('to_dict' in dir(self.review))

    def test_str(self):
        """Tests the __str__ method."""
        review_str = str(self.review)
        self.assertEqual(review_str, "[Review] ({}) {}".format(self.review.id, self.review.__dict__))


if __name__ == "__main__":
    unittest.main()
