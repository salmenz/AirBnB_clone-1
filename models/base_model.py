#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel():
    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def updated_at(self):
        return self.__updated_at
    @updated_at.setter
    def updated_at(self, value):
        self.__updated_at = value

    " TO DO "
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__)

    " TO DO "
    def save(self):
        self.updated_at = datetime.now()

    
    " TO DO "
    def to_dict(self):
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
