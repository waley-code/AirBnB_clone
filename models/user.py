#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    This creates new user with attr below

    Attributes:
          email (str): email of string type
          password (str): password of string type
          first_name (str): first_name of string type
          last_name (str): last_name of string type
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
