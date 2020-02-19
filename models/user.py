#!/usr/bin/python3


from models.base_model import BaseModel
""" class User that inherits from BaseModel
"""


class User(BaseModel):
    """ class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
