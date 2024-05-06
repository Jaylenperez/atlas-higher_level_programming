#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary and returns the new dictionary.
    If the key does not exist, the original dictionary is returned.
    """
    if key in a_dictionary:
        # Create a copy of the dictionary to avoid modifying the original
        new_dict = a_dictionary.copy()
        del new_dict[key]
        return new_dict
    else:
        # Return the original dictionary if the key does not exist
        return a_dictionary
