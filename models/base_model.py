#!/usr/bin/python3
"""
Module: base_model.py
Defines the BaseModels class with common attributes/methods.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for other models.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel instance with unique id and current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """
        Update updated_at with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary for all keys/values of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
