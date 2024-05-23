#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base # Import the Base class from the models.base module.

class Rectangle(Base): # Create Rectangle class that inherits from Base class
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None): # Create constructor. Here we pass in self, width, height, x with value 0, y with value 0, and id from base class
        super().__init__(id) # Call constructor of parent class. This initializes id of Rectangle instance and ensures that the base class initialization logic is executed.

        self.width = width # Assign values to all the parameters
        self.height = height
        self.x = x
        self.y = y

    @property # Property methods and setters are used to encapsulate access to the private instance variables.
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value
