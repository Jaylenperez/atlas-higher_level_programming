#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the highest integer value.
    If no score found, returns None.
    """
    if a_dictionary is None:
        return None

    best_key = None
    best_value = None
    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_key = key
            best_value = value
    return best_key
