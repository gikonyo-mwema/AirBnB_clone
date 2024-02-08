#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """
    Class that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = {k: BaseModel(**v) for k, v in json.load(f).items()}
        except FileNotFoundError:
            pass
