""" Contains a class that defines all common attributes/methods for other classes"""

import uuid
import datetime

class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__} "
    

    def save(self):
        """called when the object is saved"""
        self.updated_at = datetime.datetime.now()


    def to_dict(self):
        """to dict"""
        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict['updated_at'] = self.updated_at.isoformat("%Y-%m-%dT%H:%M:%S.%f")
        return obj_dict