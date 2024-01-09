#!/usr/bin/python3
"""
this is the class place that inherits from base model
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """class place inheriting"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_batrooms = 0
    max_quest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
