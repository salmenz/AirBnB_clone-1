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
        return "[<>] (<>) <>"

    " TO DO "
    def save(self):
        return
    
    " TO DO "
    def to_dict(self):
        return


