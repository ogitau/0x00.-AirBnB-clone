#!/usr/bin/python3
"""This is the base module for all the classes in this project"""

from datetime import datetime
import uuid
import models
from models import storage


class BaseModel:
    """Base class for all models"""
    def __init__(self, *args, **kwargs):
        """Instantiation of a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            try:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            except ValueError:
                try:
                    kwargs['updated_at'] = datetime.strptime(
                            kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S')
                    kwargs['created_at'] = datetime.strptime(
                            kwargs['created_at'], '%Y-%m-%dT%H:%M:%S')
                except ValueError:
                    print("Error parsing datetime strings.Using current time")
                    kwargs['updated_at'] = datetime.now()
                    kwargs['created_at'] = datetime.now()
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates instances with the current updated_at time changes"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Instances to be converted into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = str(type(self)).split('.')[-1].split('\'')[0]
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
