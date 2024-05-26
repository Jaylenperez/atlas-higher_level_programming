#!/usr/bin/python3
"""Defines a base model class."""
import json

class Base:
    """Represents the base model"""
    __nb_objects = 0 # Define class private attribute called number of objects. Initialize to 0
    def __init__(self, id=None): # Define class constructor that takes self and optional parameter ID Initialied to None
        if id is not None: # Check if ID has been provided
            self.id = id # If ID is provided, we are going to assign the value of self.ID attribute
        else:
            Base.__nb_objects += 1 # If value is not provided we increment the private class attribute by 1
            self.id = Base.__nb_objects # assign unique ID to each instance that is created from the base model class starting from each new instance or object

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        to_json = json.dumps(list_dictionaries) # change pattern object to JSON format 

        return to_json