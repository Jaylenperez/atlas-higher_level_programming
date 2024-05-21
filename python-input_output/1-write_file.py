#!/usr/bin/python3
"""module definition"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file"""
    # Open the file in write mode ('w') with UTF-8 encoding.
    # If the file doesn't exist, it will be created.
    # If it does exist, its content will be overwritten.
    with open(filename, 'w', encoding='utf-8') as f:
        # Write the text to the file.
        f.write(text)
        # Return the number of characters written.
        return len(text)
