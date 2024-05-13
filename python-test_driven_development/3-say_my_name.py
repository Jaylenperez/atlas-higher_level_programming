#!/usr/bin/python3
"""A module for printing a person's name."""

def say_my_name(first_name, last_name=""):
    """Prints a person's name.
    
    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person. Defaults to "".
        
    Raises:
        TypeError: If either first_name or last_name is not a string.
        
    Examples:
        >>> say_my_name("John", "Doe")
        My name is John Doe
        >>> say_my_name("Alice")
        My name is Alice
        >>> say_my_name(123, "Smith")
        Traceback (most recent call last):
            ...
        TypeError: first_name must be a string
        >>> say_my_name("Jane", 456)
        Traceback (most recent call last):
            ...
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is ", first_name)