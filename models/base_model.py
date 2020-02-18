#!/usr/bin/python3
import uuid
import datetime
import models
"""
This module for class BaseModel
"""


class BaseModel:
    """
    class BaseModel
    """
    def __init__(self):
        """
        Constructor of class BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        formats string representation of the BaseModel
        """
        return "[<{}>] ({}) <self.__dict__>" \
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = str(
            self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        dic['updated_at'] = str(
            self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        return dic
