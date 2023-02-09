#!/usr/bin/python3
"""
Defines a FileStorage class
"""

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """
    that serializes instances to a JSON file and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """
        returns all dict objects
        """
        return FileStorage.__objects
    
    def  new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
        
    def save(self):
        """
         serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},f
            )
        
    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON 
        file (__file_path) exists ; otherwise, do nothing. 
        """
        current_classes = {'BaseModel': BaseModel, 'User': User}
        
        if not os.path.exists(FileStorage.__file_path):
            return
        
        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None
            
            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass
            if deserialized is None:
                return
            
            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()
            }
        
    