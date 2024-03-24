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
                if v and k:
                    json_dict[k] = v.to_dict()
            json_string = json.JSONEncoder().encode(json_dict)
            file.write(json_string)

    def reload(self):
        from ..base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r") as file:
                json_string = file.read()
                if len(json_string) > 0:
                    json_dict = json.JSONDecoder().decode(json_string)
                    for k, v in json_dict.items():
                        name = k.split(".")
                        FileStorage.__objects[k] = eval(
                            "{}(**v)".format(name[0]))
        except FileNotFoundError:
            pass
