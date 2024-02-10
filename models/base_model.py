#!/usr/bin/python3
"""
Module: base_model.py
Defines the BaseModels class with common attributes/methods.
"""


import uuid
from datetime import datetime
 


class BaseModel:
    """
    Base class for othr models.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize Basemodel instance with unique id and current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.name = "My_First_Model"
            self.register()

    def register(self):
        """
        Register the instance in storage
        """
        from models import storage
        storage.new(self)

    def save(self):
        """
        Update update_at with current datetime
        """
        self.updated_at = datetime.now()
        self.persist()

    def persist(self):
        """
        Persist the instance in storage
        """
        from models import storage
        storage.save()

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
        Return a string representation fo the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
