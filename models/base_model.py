#!/usr/bin/python3

""" Base Model class """

import uuid
from datetime import datetime
import models
class BaseModel:
    """Base Class """
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs["created_at"] =datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] =datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
            
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
        