#!/usr/bin/python3
"""
Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Inherits BaseModel class

     Attributes:
        city_id (str): City id
        user_id (str): User id
        name (str): place name
        description (str): description 
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms 
        max_guest (int): maximum number of guests 
        price_by_night (int): price by night 
        latitude (float): latitude 
        longitude (float): longitude 
        amenity_ids (list): list of Amenity ids

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
