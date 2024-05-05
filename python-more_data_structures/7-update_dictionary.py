#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Updates a dictionary by adding or replacing a key/value pair.

    Args:
    a_dictionary (dict): The dictionary to update.
    key (str): The key to add or update.
    value: The value to set for the key.

    Returns:
    dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
