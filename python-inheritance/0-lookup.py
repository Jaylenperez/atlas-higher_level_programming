#!/usr/bin/python3

"""
This module provides utility functions for working with lists.
"""


def lookup(obj):

    """
    This function takes an object as input and returns a list
    of its attributes and methods.

    Parameters:
    obj (object): The object whose attributes and methods are to be listed.

    Returns:
    list: A list of the object's attributes and methods.
    """
    return dir(obj)


# Example usage
if __name__ == "__main__":
    lookup = __import__('0-lookup').lookup

    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
