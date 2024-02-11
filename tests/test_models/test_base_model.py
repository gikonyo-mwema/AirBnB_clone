#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel class.
"""

import unittest
import datetime
from models.base_model import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def setUp(self):
        """Set up the test case."""
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_instantiation(self):
        """Test the instantiation of a BaseModel instance."""
        self.assertIsInstance(self.model1, BaseModel)
        self.assertIsInstance(self.model1.id, str)
        self.assertIsInstance(self.model1.created_at, datetime.datetime)
        self.assertIsInstance(self.model1.updated_at, datetime.datetime)
        self.assertIn(self.model1, storage.all().values())
        self.assertNotEqual(self.model1.id, self.model2.id)
        self.assertLess(self.model1.created_at, self.model2.created_at)
        self.assertLess(self.model1.updated_at, self.model2.updated_at)

    def test_str(self):
        """Test the string representation of a BaseModel instance."""
        self.assertEqual(str(self.model1), f"[BaseModel] ({self.model1.id}) {self.model1.__dict__}")

    def test_to_dict(self):
        """Test the to_dict method of a BaseModel instance."""
        model_dict = self.model1.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], self.model1.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.model1.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model1.updated_at.isoformat())
        self.assertNotEqual(model_dict, self.model1.__dict__)

    def test_save(self):
        """Test the save method of a BaseModel instance."""
        old_updated_at = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, old_updated_at)

    def tearDown(self):
        """Tear down the test case."""
        self.model1 = None
        self.model2 = None

if __name__ == '__main__':
    unittest.main()
