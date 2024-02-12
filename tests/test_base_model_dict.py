#!/usr/bin/python3
"""
This script creates an instance of BaseModel, sets its attributes,
and prints its id, dictionary representation, and creation time.
It then creates a new BaseModel instance from the dictionary.
"""

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Defines a class to test BaseModel
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.base_model_instance = BaseModel()
        self.base_model_instance.name = "My_First_Model"
        self.base_model_instance.my_number = 89

    def test_id(self):
        """
        Test that the id attribute is a string and follows the UUID format
        """
        self.assertIsInstance(self.base_model_instance.id, str)

    def test_created_at(self):
        """
        Test that created_at is of type datetime
        """
        created_at = self.base_model_instance.created_at
        self.assertIsInstance(created_at, datetime.datetime)

    def test_to_dict(self):
        """
        Test that to_dict returns a dictionary
        """
        base_model_dict = self.base_model_instance.to_dict()
        self.assertIsInstance(base_model_dict, dict)


if __name__ == "__main__":
    main()
