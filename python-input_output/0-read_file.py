#!/usr/bin/python3
"""This module defines a file-reading function"""

# Defines the read_file function that takes one parameter, filename,
# with a default value of an empty string.

# This means if the function is called without providing a filename,
# it will attempt to read from a file named after the default value,
# which would be an empty string


def read_file(filename=""):
    """Prints the contents of UTF8 text file"""

    # Opens the file specified by filename
    # in read mode with UTF-8 encoding.

    # The 'with' statement ensures the file
    # is properly closed after operations are completed.
    with open(filename, encoding="utf-8") as f:

        # Reads entire content of the file into a string.
        # The print function then outputs this content to the console.
        # The 'end=""' parameter prevents adding a newline
        # character at the end of the printed content,
        # so the output continues on the same line.
        print(f.read(), end="")
