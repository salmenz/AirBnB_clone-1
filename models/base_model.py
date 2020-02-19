#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


""" BaseModel that defines all common attributes/methods for other classes."""


class BaseModel():
    """ BaseModel that defines all
    common attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        if kwargs is None:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            storage.new()
        else:
            for k, v in kwargs.items():
                if "__class__" != k:
                    if k in ("created_at", "updated_at"):
                        setattr(self, k, datetime.strptime(v,
                                "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, k, v)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of
        the instance:
        """
        my_dict = {}
        for i in self.__dict__.keys():
            name = i.split("__")
            if len(name) > 1:
                name = i.split("__")[1]
            else:
                name = i.split("__")[0]
            if name in ("updated_at", "created_at"):
                my_dict[name] = datetime.strftime(self.__dict__[i],
                                                  "%Y-%m-%dT%H:%M:%S.%f")
            else:
                my_dict[name] = self.__dict__[i]
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
