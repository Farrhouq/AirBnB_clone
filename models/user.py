#!/usr/bin/python3
"""This module contains the User class"""

from .base_model import BaseModel


class User(BaseModel):
    """A user class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
