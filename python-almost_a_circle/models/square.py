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

    @property
    def size(self):
        """
        Get/set the size of the Square.
        """
        return self.width # Directly returning the width attribute, which represents the size of the square

    @size.setter
    def size(self, value):
        self.width = value # Setting the width attribute to the provided value
        self.height = value # Additionally, setting the height attribute to the same value to ensure the square remains a perfect square.

    def __str__(self):
        """
        Str representation
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, # Using the format method to construct a string that includes the class name "Square"
                                                 self.width) # followed by the instance's ID, x-coordinate, y-coordinate, and width (side length)

    def update(self, *args, **kwargs):
        """
        Update the Square.
        """
        if args and len(args) != 0: # If the positional argument that is passed is not empty
            for count, arg in enumerate(args): # Iterate through the positional arguments
                if count == 0: # Assign the first  positional argument to id
                    self.id = arg
                elif count == 1: # Assign the second positional argument to size
                    self.size = arg
                elif count == 2: # Assign the third positional argument to x
                    self.x = arg
                elif count == 3: # Assign the fourth positional argument to y
                    self.y = arg
                else: continue # Skip any additional positional arguments beyond four

        elif len(kwargs) > 0: # If the positional argument passed is empty
            for key, value in kwargs.items(): # Iterate through the keyword arguments
                if key == "id": # Assign the 'id' keyword argument to self.id
                    self.id = value
                elif key == "size": # Assign the 'size' keyword argument to both width and height
                    self.width = value
                    self.height = value
                elif key == "x": # Assign the 'x' keyword argument to self.x
                    self.x = value
                elif key == "y": # Assign the 'y' keyword argument to self.y
                    self.y = value
                else: # Break the loop if a non-matching keyword argument is encountered
                    break

    def to_dictionary(self):
            """Return the dictionary representation of the Square."""
            square_dict = {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }

            return square_dict

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)  