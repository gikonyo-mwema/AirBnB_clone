#!/usr/bin/env python3
"""
Module: file_storage.py
Defines the FileStorage class for serializing and deserializing
instances to/from a JSON file.
"""


import os
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
        return self.__objects

    def new(self, obj):
        """
        Sets obj in _objects with key <obj class name>.id.
        """
        if not hasattr(obj, 'id'):
            raise ValueError("Object must have an 'id' attribute")
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        (Using the path specified in __file_path).
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            # print(f"Object: {obj}, Type: {type(obj)}")
            if hasattr(obj, "to_dict"):  # Check if to_dict method exists
                serialized_objects[key] = obj.to_dict()

        with open(self.__file__path, "w") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """
        Deserializes the JSON file back into __objects.
        Only if the JSON file (__file_path) exists; otherwise, do nothing
        """
        if not os.path.exists(self.__file__path):
            return  # If the file doesn't exist, do nothing

        with open(self.__file__path, "r") as json_file:
            serialized_objects = json.load(json_file)
            for key, serialized_obj in serialized_objects.items():
                class_name, obj_id = key.split(".")
                class_dict = {
                        "BaseModel": BaseModel,
                        "User": User,
                        "State": State,
                        "City": City,
                        "Place": Place,
                        "Amenity": Amenity,
                        "Review": Review
                }  # Add other classes
                if class_name in class_dict:
                    Class = class_dict[class_name]
                    obj = Class(**serialized_obj)  # Create a new instance
                    self.__objects[key] = obj
                else:
                    raise ValueError(f"Unknown class name: {class_name}")
