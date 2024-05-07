#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Attempt to format the value as an integer and print it
        print("{:d}".format(value))
        # If successful, return True
        return True
    except (ValueError, TypeError):
        # If a ValueError occurs (meaning the value couldn't be formatted as an integer), return False
        return False
