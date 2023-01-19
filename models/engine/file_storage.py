#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }

class FileStorage:
    """ class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        "all"
        if cls is None:
            return self.__objects
        else:
            return {k: v for k, v in self.__objects.items() if k.split(".")[0] == cls.__name__} #
    
    def new(self, obj):
        """ new """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(self.__file_path, 'w+', encoding='utf-8') as fp:
            fp.write(json.dumps({k: v.to_dict() for k, v in self.__objects.items()}))
            
    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as fp: # 
                file_data = fp.read() 
                jason_data = json.loads(file_data)
                {self.new(BaseModel(**v)) for k, v in jason_data.items()} # 
        else:
            return
    
    def delete(self, obj=None):
        """ delete """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
                self.save()