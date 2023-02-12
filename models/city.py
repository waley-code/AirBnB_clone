#!/usr/bin/python3
"""
This module contains the City class and attr
inheriting from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This creates new City with attr below

    Attributes:
          state_id (str): state_id of string type
          name (str): name of string type
    """
    state_id = ""
    name = ""
