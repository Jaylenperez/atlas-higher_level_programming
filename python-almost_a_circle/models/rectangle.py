#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base # Import the Base class from the models.base module.

class Rectangle(Base): # Create Rectangle class that inherits from Base class
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None): # Constructor initializing rectangle with dimensions and position
        super().__init__(id) # Call parent class constructor to initialize ID

        self.width = width # Set width of rectangle
        self.height = height # Set height of rectangle
        self.x = x # Set x-coordinate of rectangle
        self.y = y # Set y-coordinate of rectangle

    @property # Property methods and setters are used to encapsulate access to the private instance variables.
    def width(self):
        """Gets the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int): # Ensure value is an integer
            raise TypeError("width must be an integer")
        if value <= 0: # Width must be positive
            raise ValueError("width must be > 0")
        self.__width = value # Update width

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int): # Ensure height is an integer
            raise TypeError("height must be an integer")
        if value <= 0: # height must be positive
            raise ValueError("height must be > 0")
        self.__height = value # Update height

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int): # Ensure that value is an integer
            raise TypeError("x must be an integer")
        if value < 0: # x must be positive
            raise ValueError("x must be >= 0")
        self.__x = value # Update x

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int): # Ensure value is an integer
            raise TypeError("y must be an integer")
        if value < 0: # y must be positive
            raise ValueError("y must be >= 0")
        self.__y = value # Update y

    def area(self):
        """
        Returns area of rectangle
        """
        area = self.width * self.height
        
        return area
