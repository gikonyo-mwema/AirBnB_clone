#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel class.
"""

import unittest
import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_no_args_instantiates(self):
        """
        Test if creating an instance without any arguments
        results in a BaseModel instance.
        """
        self.assertIsInstance(self.model1, BaseModel)

    def test_new_instance_stored_in_objects(self):
        """
        Test if a newly created instance is stored in the
        appropriate storage mechanism.
        """
        self.assertIn(self.model1, storage.all().values())

    def test_id_is_public_str(self):
        """
        Test if the id attribute is a string.
        """
        self.assertIsInstance(self.model1.id, str)

    def test_created_at_is_public_datetime(self):
        """
        Test if the created_at attribute is of type datetime.
        """
        self.assertIsInstance(self.model1.created_at, datetime.datetime)

    def test_updated_at_is_public_datetime(self):
        """
        Test if the updated_at attribute is of type datetime.
        """
        self.assertIsInstance(self.model1.updated_at, datetime.datetime)

    def test_two_models_unique_ids(self):
        """
        Test if two instances have different IDs.
        """
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_two_models_different_created_at(self):
        """
        Test if two instances created at different times have
        distinct created_at attributes.
        """
        self.assertLess(self.model1.created_at, self.model2.created_at)

    def test_two_models_different_updated_at(self):
        """
        Test if two instances updated at different times have
        distinct updated_at attributes.
        """
        self.assertLess(self.model1.updated_at, self.model2.updated_at)

    def test_str_representation(self):
        """
        Test the string representation of a BaseModel instance.
        """
        expected_str = f"[BaseModel] ({self.model1.id}) {self.model1.__dict__}"
        self.assertEqual(str(self.model1), expected_str)

    def test_to_dict_type(self):
        """
        Test if the return value of to_dict is a dictionary.
        """
        model_dict = self.model1.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """
        Test if the dictionary returned by to_dict contains
        the expected keys.
        """
        model_dict = self.model1.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        """
        Test if created_at and updated_at in the dictionary are strings.
        """
        model_dict = self.model1.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_save_updates_file(self):
        """
        Test if calling save updates the corresponding file
        and includes the instance's ID.
        """
        old_updated_at = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, old_updated_at)

    def tearDown(self):
        """
        Tear down the test case.
        """
        self.model1 = None
        self.model2 = None


if __name__ == '__main__':
    unittest.main()
