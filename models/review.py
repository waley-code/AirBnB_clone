#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This stores reviews related to attr below

    Attributes:
          place_id (str): place_id of string type
          user_id (str): user_id of string type
          text (str): text of string type
    """
    place_id = ""
    user_id = ""
    text = ""
