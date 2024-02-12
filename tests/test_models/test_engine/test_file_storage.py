import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Defines a set of test for the FileStorage class
    """

    def setUp(self):
        """
        Sets up the tests
        """
        self.storage = FileStorage()
        self.model1 = BaseModel()
        self.model1.name = "ALX"
        self.model1.my_number = 89
        self.storage.new(self.model1)
        self.model2 = BaseModel()

    def tearDown(self):
        """
        Ends the test
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Tests the all method of FileStorage
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """
        Tests the new method of FileStorage
        """
        self.storage.new(self.model2)
        self.assertIn("BaseModel." + self.model2.id, self.storage.all())

    def test_save(self):
        """
        Tests the save method of FileStorage
        """
        storage = FileStorage()
        model = BaseModel()
        model.name = "ALX"
        model.my_number = 89
        storage.new(model)
        self.storage.save()
        with open("file.json", "r") as file:
            self.assertIn("BaseModel." + self.model1.id, file.read())

    def test_reload(self):
        """
        Tests the reload method of FileStorage
        """
        storage = FileStorage()
        model = BaseModel()
        model.name = "ALX"
        model.my_number = 89
        storage.new(model)
        storage.save()
        self.storage.reload()
        self.assertIn("BaseModel." + self.model1.id, self.storage.all())


if __name__ == '__main__':
    unittest.main()
