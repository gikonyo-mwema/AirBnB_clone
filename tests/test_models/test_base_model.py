"""
This module contains unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Defines tests for class BaseModel
    """

    def setUp(self):
        """
        Sets up the tests
        """
        self.model1 = BaseModel()
        self.model1.name = "ALX"
        self.model1.my_number = 89

    def tearDown(self):
        """
        Ends the test
        """
        pass

    def test_attributes(self):
        """
        Tests the attributes of BaseModel
        """
        self.assertTrue(hasattr(self.model1, "name"))
        self.assertTrue(hasattr(self.model1, "my_number"))
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "updated_at"))
        self.assertTrue(hasattr(self.model1, "id"))

    def test_save(self):
        """
        Tests the save method of BaseModel
        """
        old_updated_at = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(old_updated_at, self.model1.updated_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of BaseModel
        """
        model1_dict = self.model1.to_dict()
        self.assertEqual(self.model1.__class__.__name__, 'BaseModel')
        self.assertEqual(model1_dict["__class__"], 'BaseModel')
        self.assertEqual(model1_dict["name"], "ALX")
        self.assertEqual(model1_dict["my_number"], 89)
        self.assertTrue(isinstance(model1_dict["created_at"], str))
        self.assertTrue(isinstance(model1_dict["updated_at"], str))


if __name__ == '__main__':
    unittest.main()


