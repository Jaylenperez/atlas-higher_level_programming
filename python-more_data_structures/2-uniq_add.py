#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in 'my_list' and returns the sum.

    Args:
    my_list (list): A list of integers.

    Returns:
    int: The sum of all unique integers in 'my_list'.
    """
    # Use a set to store unqiue integers and then sum them
    unique_sum = sum(set(my_list))
    return unique_sum
