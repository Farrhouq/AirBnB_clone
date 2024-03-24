#!/usr/bin/python3
""" Contains a class that defines all common attributes/methods for
other classes"""

import uuid
import datetime
from models import storage


class BaseModel:
    """defines all common attributes/methods for other classes"""

    # def __init__(self):
    #     self.id = str(uuid.uuid4())
    #     self.created_at = datetime.datetime.now()
    #     self.updated_at = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        """instantiating a new model with the given attributes"""

        if kwargs:
            self.id = kwargs['id']
            self.updated_at = datetime.datetime.fromisoformat(
                kwargs['updated_at'])
            self.created_at = datetime.datetime.fromisoformat(
                kwargs['created_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
            print(self.id)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """called when the object is saved"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """to dict"""
        obj_dict = dict(self.__dict__)
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
