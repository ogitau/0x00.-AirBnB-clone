#!/usr/bin/python3
"""
a class that inherits from basemodel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """the user class inheriting from base model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
