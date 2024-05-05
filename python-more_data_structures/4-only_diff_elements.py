#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one of the input sets.

    Args:
    set_1 (set): The first set of elements.
    set_2 (set): The second set of elements.

    Returns:
    set: A set of all elements present in only one of the input sets.
    """
    # Use the symmetric_difference method to find elements present in only one set
    diff_elements = set_1.symmetric_difference(set_2)
    return diff_elements
