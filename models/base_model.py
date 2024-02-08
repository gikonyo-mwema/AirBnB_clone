#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:
    """
    Class that defines all common methods/attributes for other classes
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
            self.created_at = self.updated_at = datetime.now()
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
        return {**self.__dict__,
                "__class__": self.__class__.__name__,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()}

    def __str__(self):
        """
        Return a string representation fo the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
