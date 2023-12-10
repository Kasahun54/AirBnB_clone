#!/usr/bin/python3
"""
The entire project the entry point
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """All the classes in the AirBnb console project

    Arttributes:
        id(str): unique user identity
        created_at: current datetime
        updated_at: updated current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save: updates instance arttributes
        to_dict(self): returns the dictionary values

    """

    def __init__(self, *args, **kwargs):
        """Public instance artributes initialization

        Args:
            *args(args): arguments
            **kwargs(dict): attrubute values

        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Returns string
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - by current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all 
        keys/values of __dict__ instance
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
