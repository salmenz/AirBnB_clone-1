#!/usr/bin/python3
import json
from os import path


""" that serializes instances to a JSON file and
    deserializes JSON file to instances """


class FileStorage():
    """ that serializes instances to a JSON file and
    deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for i in self.all():
            new_dict[i] = self.all()[i].to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(new_dict))

    def reload(self):
        """ reserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised) """
        try:
            from models.base_model import BaseModel
            from models.user import User
            with open(self.__file_path) as file:
                data = json.loads(file.read())
                for k, i in data.items():
                    key = k.split(".")[0]
                    obj = eval(key)(**i)
                    self.new(obj)
        except Exception:
            pass
