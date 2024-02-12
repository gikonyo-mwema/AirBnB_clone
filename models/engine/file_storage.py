#!/usr/bin/env python3
"""
Module: file_storage.py
Defines the FileStorage class for serializing and deserializing
instances to/from a JSON file.
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Handles serialization and deserialization of instances to/from JSON
    """

    def __init__(self):
        """
        Initializes FileStorage instance with private attributes.
        """
        self.__file__path = "file.json"  # Path to the JSON file
        self.__objects = {}  # Dictionary to store objects

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets obj in _objects with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        (Using the path specified in __file_path).
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """
        Deserializes the JSON file back into __objects.
        Only if the JSON file (__file_path) exists; otherwise, do nothing
        """
        try:
            with open(self.__file_path, "r") as json_file:
                serialized_objects = json.load(json_file)
                for key, serialized_obj in serialized_objects.items():
                    class_name, obj_id = key.split(".")
                    # Assuming you have a method tha creats instances
                    # from a dictionary
                    obj = create_instance_from_dict(class_name, serialized_obj)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass  # If the file doesn't exist, no exception should be raised
