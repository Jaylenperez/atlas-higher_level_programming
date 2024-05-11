#!/usr/bin/python3

"""
This module defines a Square class for geometric calculations.
"""


class Square:
    """
    Represents a square with a given size.

    Attributes:
        _Square__size (int): The length of a side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The length of a side of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be an integer")
        self._Square__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._Square__size ** 2
