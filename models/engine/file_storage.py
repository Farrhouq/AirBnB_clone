#!/usr/bin/python3
"""Contains a a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances"""

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """return a list of objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """save an object"""

        if obj:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes the __objects and save it to the file"""
        import json
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json_dict = {}
            for k, v in FileStorage.__objects.items():
                print(k, v)
                if v and k:
                    json_dict[k] = v.to_dict()
            json_string = json.JSONEncoder().encode(json_dict)
            file.write(json_string)


    def reload(self):
        """reload all objects only if the file exists"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except Exception as e:
            pass
