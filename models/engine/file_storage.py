#!/usr/bin/python3
"""Contains a a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances"""

import json

class FileStorage:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """return a list of objects"""
        return self.__objects
    
    def new(self, obj):
        """save an object"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """save all objects"""
        with open(self.__file_path, "w") as f:
            # print(self.__objects)
            json.dump(self.__objects, f)

    def reload(self):
        """reload all objects only if the file exists"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except Exception as e:
            pass
