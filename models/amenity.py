#!/usr/bin/python3
"""
This module contains the Amenity class and attr
inheriting from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This creates Amenities with attr below

    Attributes:
        name (str): name of string type
    """
    name = ""
