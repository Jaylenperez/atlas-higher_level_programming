#!/usr/bin/python3
"""Module for printing a square with the character '#"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if size is a float less than 0.
        ValueError: If size is less than 0.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: ./4-main.py <size>")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
        print_square(size)
    except ValueError:
        print("Size must be an integer.")

