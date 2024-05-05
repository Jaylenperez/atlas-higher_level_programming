#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Returns a set of common elements between 'set_1' and 'set_2'.

    Args:
    set_1 (set): The first set of elements.
    set_2 (set): The second set of elements.

    Returns:
    set: A set of common elements between 'set_1' and 'set_2'.
    """
    # Use the intersection method to find common elements
    common = set_1.intersection(set_2)
    return common
