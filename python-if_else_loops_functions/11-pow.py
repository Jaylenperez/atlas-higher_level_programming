#!/usr/bin/python3

def pow(a, b):
    """
    Calculate the power of a to the power of b.

    Parameters:
    a (int or float): The base.
    b (int): The exponent.

    Returns:
    float: The result of a raised to the power of b.
    """
    result = 1
    for _ in range(abs(b)):
        result *= a
    return result if b >= 0 else 1 / result
