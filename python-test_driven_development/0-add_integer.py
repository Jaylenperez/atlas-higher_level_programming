#!/usr/bin/python3
"""
Module for add_integer method.
"""

def add_integer(a, b=98):
    """
    Adds two integers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 0.
        
    Raises:
        TypeError: TypeError: If a or b is not an integer or float.
        
    Returns:
        int: The sum of a and b.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))