#!/usr/bin/python3
"""This module defines a JSON file-writing function"""
import json


# my_obj is the object we want to write to a file in JSON format.
# filename is the name of the file where we want to store the JSON data.
def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON format"""

    # Open the file specified by filename in write mode ('w').
    # The 'with' statement ensures the file is properly closed after operations complete.
    with open(filename, "w") as f:

        # Use json.dump() to write the JSON representation of my_obj to the file.
        # json.dump() takes two arguments: the object to serialize and the file object to write to.
        json.dump(my_obj, f)
