#!/usr/bin/python3
"""This module defines a Python class-to-JSON function"""

# Define a function named class_to_json that takes one parameter: obj.
# This parameter represents the object we want to convert to a dictionary.
def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    
    # Access the __dict__ attribute of the object.
    # __dict__ is a special attribute in Python classes that stores an object's writable attributes.
    # This effectively gives us a dictionary representation of the object's state.
    return obj.__dict__
