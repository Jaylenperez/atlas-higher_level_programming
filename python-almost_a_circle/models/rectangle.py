#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base # import base from Base class.

class Rectangle(Base): # Create Rectangle class. Here we pass the base model which means Rectangle will inherit from base class
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None): # Create constructor. Here we pass in self, width, height, x with value 0, y with value 0, and id from base class
        super().__init__(id) # Call constructor of parent class. Here we call super and pass in id. This will initialize the id attribute of the Rectangle instance. Ensures the base class initialization logic is executed when creating a rectangle instance.

        self.width = width # assign values to all the parameters
        self.height = height
        self.x = x
        self.y = y

    @property
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
