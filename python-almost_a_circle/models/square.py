#!/usr/bin/python3
"""
Module for square class
"""
from models.rectangle import Rectangle # Importing the Rectangle class for inheritance


class Square(Rectangle): # Defining a square class inheriting from Rectangle
    """
    The Square class
    """
    def __init__(self, size, x=0, y=0, id=None): # Constructor for creating a square instance
        """
        Square class constructor
        """
        super().__init__(size, size, x, y, id) # Calling the parent class constructor with size for both width and height
    
    def __str__(self):
        """
        Str representation
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, # Using the format method to construct a string that includes the class name "Square"
                                                 self.width) # followed by the instance's ID, x-coordinate, y-coordinate, and width (side length)
