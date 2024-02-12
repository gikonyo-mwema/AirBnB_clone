#!/usr/bin/python3
""" Define unittest for user"""

import unittest
import datetime
from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """
    Defines unit tests for the User class.
    """

    def setUp(self):
        """
        Sets up the tests.
        """
        self.user1 = User()
        self.user2 = User()

    def test_no_args_instantiates(self):
        """
        Test if creating an instance without any arguments
        results in a User instance.
        """
        self.assertIsInstance(self.user1, User)

    def test_new_instance_stored_in_objects(self):
        """
        Test if a newly created instance is stored in the
        appropriate storage mechanism.
        """
        self.assertIn(self.user1, storage.all().values())

    def test_id_is_public_str(self):
        """
        Test if the id attribute is a string.
        """
        self.assertIsInstance(self.user1.id, str)

    def test_created_at_is_public_datetime(self):
        """
        Test if the created_at attribute is of type datetime.
        """
        self.assertIsInstance(self.user1.created_at, datetime.datetime)

    def test_updated_at_is_public_datetime(self):
        """
        Test if the updated_at attribute is of type datetime.
        """
        self.assertIsInstance(self.user1.updated_at, datetime.datetime)

    def test_two_models_unique_ids(self):
        """
        Test if two instances have different IDs.
        """
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_two_models_different_created_at(self):
        """
        Test if two instances created at different times have
        distinct created_at attributes.
        """
        self.assertLess(self.user1.created_at, self.user2.created_at)

    def test_two_models_different_updated_at(self):
        """
        Test if two instances updated at different times have
        distinct updated_at attributes.
        """
        self.assertLess(self.user1.updated_at, self.user2.updated_at)

    def test_str_representation(self):
        """
        Test the string representation of a User instance.
        """
        expected_str = f"[User] ({self.user1.id}) {self.user1.__dict__}"
        self.assertEqual(str(self.user1), expected_str)

    def test_to_dict_type(self):
        """
        Test if the return value of to_dict is a dictionary.
        """
        user_dict = self.user1.to_dict()
        self.assertIsInstance(user_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """
        Test if the dictionary returned by to_dict contains
        the expected keys.
        """
        user_dict = self.user1.to_dict()
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        """
        Test if created_at and updated_at in the dictionary are strings.
        """
        user_dict = self.user1.to_dict()
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

    def test_save_updates_file(self):
        """
        Test if calling save updates the corresponding file
        and includes the instance's ID.
        """
        old_updated_at = self.user1.updated_at
        self.user1.save()
        self.assertNotEqual(self.user1.updated_at, old_updated_at)

    def tearDown(self):
        """
        Tear down the test case.
        """
        self.user1 = None
        self.user2 = None


if __name__ == '__main__':
    unittest.main()
