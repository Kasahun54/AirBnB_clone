#!/usr/bin/python3
"""
State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state

    Attributes:
        name (str): name of the state

    """
    name = ""
