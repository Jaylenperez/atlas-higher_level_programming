#!/usr/bin/python3
"""This module defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file."""

    # Opens the file specified by filename in append mode ('a').
    # The 'with' statement ensures the file is properly closed
    # after operations are completed.
    # If the file doesn't exist, it will be created.
    with open(filename, "a", encoding="utf-8") as f:

        # Appends the text to the end of the file.
        # The write method returns the number of characters written.
        # This value is immediately returned by the append_write func.
        return f.write(text)
