#!/usr/bin/python3
"""
a class city that inherits from base model
"""

from models.base_model import BaseModel


class City(BaseModel):
    """the city class that inherits from base model"""

    state_id = ""
    name = ""
