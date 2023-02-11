#!/usr/bin/python3
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
