#!/usr/bin/python3
"""This module contains the State class"""

from .base_model import BaseModel


class Review(BaseModel):
    """A amenity class"""

    place_id = ""
    user_id = ""
    text = ""
