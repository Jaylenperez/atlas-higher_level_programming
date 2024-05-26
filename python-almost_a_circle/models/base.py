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

    @staticmethod # Serialize 
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        to_json = json.dumps(list_dictionaries) # change pattern object to JSON format 

        return to_json
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): List of instances who inherts of Base
        """
        file_name = "{}.json".format(cls.__name__)

        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(list_dict))

    def from_json_string(json_string): # Deserialize string
        """
        
        """
        if json_string is None or json_string == "[]": # If json string is empty
            return [] # Return empty python list
        return json.loads(json_string) # Else, we should 

    @classmethod
    def create(cls, **dictionary):
        """Returns an instancce with all attributes already set.
        """
        if dictionary and dictionary != {}: # if dictionary is present and not empty
            if cls.__name__ == "Rectangle": # check if class name is coming from Rectangle class
                dummy = cls(1, 1) # dummy instance. pass in values of width and height
            else: # If it is not a rectangle it is a square
                dummy = cls(1)
            dummy.update(**dictionary) # use update method to apply values from dictionaries

            return dummy
