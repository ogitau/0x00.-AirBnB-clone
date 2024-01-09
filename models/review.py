#!/usr/bin/python3
"""
reviewclass inheritting from base model
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class review inheritting"""
    place_id = ""
    user_id = ""
    text = ""
