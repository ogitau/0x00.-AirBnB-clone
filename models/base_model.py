#!/usr/bin/python3
"""This is the base module for all the classes in this project"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all models"""
    def __init__(self, *args, **kwargs):
        """instantiation of a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
             kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
             del kwargs['__class__']
             self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string rep of an instance"""
        cls = (str(type(self)).split('.')[-1].split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates instances with the current updated_at time changes"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """instances to be converted into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.updated({'__class__':
                            (str(type(self)).split('.')[-1]).split('\'')[0]})
       dictionary['created_at'] = self.created_at.isoformat()
       dictionary['updated_at'] = self.updated_at.isoformat()
       return dictionary