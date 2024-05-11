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
            size (int, optional): The length of a side of the square.
            Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
            int: The size of the square.
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._Square__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.

        If size is equal to 0, prints an empty line.
        """
        if self._Square__size == 0:
            print()
        else:
            for i in range(self._Square__size):
                print("#" * self._Square__size)
