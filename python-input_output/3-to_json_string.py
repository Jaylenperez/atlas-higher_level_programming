#!/usr/bin/python3
"""This module defines string to JSON function"""
import json


# This parameter represents the object we want to convert to a JSON string.
def to_json_string(my_obj):
    """Returns the JSON representation of a string object"""

    # Use the json.dumps() function to convert the input object to JSON formatted string.
    # json.dumps() takes the object and returns a stirng in JSON format.
    return json.dumps(my_obj)
