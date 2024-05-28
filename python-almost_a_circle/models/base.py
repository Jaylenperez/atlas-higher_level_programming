#!/usr/bin/python3
"""Defines a base model class."""
import json

class Base:
    """
    A Base class that assigns a unique ID to each instance upon creation.

    This class serves as a foundation for other classes, automatically assigning a unqiue identifier to each instance.
    The ID is incremented for each new instance, ensuring uniqueness across all instances of derived classes.

    Attributes:
        __nb_objects (int): A private class attribute that keeps track of the number of instances created.
        It is initialized to 0 and incremented each time a new instance is created without a specified ID.
    
    Methods:
        __init__(self, id=None): Initializes a new instance of the class. If an ID is provided, it is assigned to the instance;
                                otherwise, a unique ID is generated based on the current count of instances.
        to_json_string(list_dictionaries): Returns the JSON string representation of list_dictionaries.
        save_to_file(cls, list_objs): Writes the JSON string representation of list_objs to a file.
        from_json_string(json_string): Deserializes a JSON string into a Python object.
        create(cls, **dictionary): Returns an instance with all attributes already set.
        load_from_file(cls): Loads a list of instances from a JSON file.
    """

    __nb_objects = 0 # Initialize private attribute to keep track of number of instances created.

    def __init__(self, id=None): # Constructor method for the Base class
        """
        Initializes a new instance of the class. If an ID is provided, it is assigned to the instance;
        otherwise, a unique ID is generated based on the current count of instances.
        """
        if id is not None: # Check if ID has been provided
            self.id = id # If ID is provided, we are going to assign the value of self.ID attribute
        else:
            Base.__nb_objects += 1 # If value is not provided we increment the private class attribute by 1
            self.id = Base.__nb_objects # assign unique ID to each instance that is created from the base model class starting from each new instance or object

    @staticmethod # Stacic method to convert a list of dictionaries into a JSON string. Serialize
    def to_json_string(list_dictionaries):
        """
        Serializes a list of dictionaries into a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to serialize.

        Returns:
            str: JSON string representation of the input list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []: # Returning an empty JSON array string if the input is None or an empty list.
            return "[]"
        to_json = json.dumps(list_dictionaries) # Converting the list of dictionaries to a JSON formatted string 

        return to_json
    
    @classmethod # Class method to save a list of objects to a JSON file
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to serialize and save to a file.
        """
        file_name = "{}.json".format(cls.__name__) # Constructing the filename based on the class name.

        with open(file_name, "w") as jsonfile: # Opening the file in write mode and writing the serialized objects to it.
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary()) # Assuming each object has a to_dictionary() method
                jsonfile.write(Base.to_json_string(list_dict))

    def from_json_string(json_string): # Deserialize JSON string into a Pythin object
        """
        Deserialize a JSON sting into a Python object.

        Args:
            json_string (str): JSON string to deserialize.
        
        Returns:
            list: List of deserialized objects.
        """
        if json_string is None or json_string == "[]": # If json string is empty
            return [] # Return empty python list
        return json.loads(json_string) # Deserializing the JSON string into a Python object

    @classmethod # Class method to create an instance with all attributes already set using a dictionary
    def create(cls, **dictionary):
        """
        Creates an instance with all attributes already set using a dictionary.

        Args:
            dictionary (dict): Dictionary containing key-value pairs representing the attributes and their values.
        
        Returns:
            instance: An instance of the class with attributes set according to the dictionary.
        """
        if dictionary and dictionary != {}: # if dictionary is present and not empty
            if cls.__name__ == "Rectangle": # check if class name is coming from Rectangle class
                dummy = cls(1, 1) # dummy instance. pass in values of width and height
            else: # If it is not a rectangle it is a square
                dummy = cls(1)
            dummy.update(**dictionary) # use update method to apply values from dictionaries

            return dummy

    @classmethod # Responsible for loading a lsit of instances from a JSON file 
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: List of instances loaded from the file.
        """
        file_name = "{}.json".format(cls.__name__) # Constructing the filename based on the class name

        try:
            with open(file_name, "r") as jsonfile: # Attempting to open the file in read mode and reading its content.
                list_dicts = Base.from_json_string(jsonfile.read()) # Deserializing the file content into a list of dictionaries

                list_instances = []

                for d in list_dicts: # Creating instances for each dictionary in the list and appending them to the result list
                    list_instances.append(cls.create(**d))
                return list_instances
        except FileNotFoundError:
            return [] # Returning an empty list if the file does not exist.
