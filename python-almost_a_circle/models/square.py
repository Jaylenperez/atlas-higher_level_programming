#!/usr/bin/python3
"""
Module for square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class constructor
        """
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """
        Str representation
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
