#!/usr/bin/python3
def safe_print_division(a, b):
    # Initialize the result variable
    result = None
    try:
        # Perform the division
        result = a / b
    except ZeroDivisionError:
        # If ZeroDivisionError occurs, set result to None
        pass
    finally:
        # Print the result inside the finally block to ensure it's printed regardless of whether an exception occured
        print("Inside result: {}".format(result))
    # Return the result
    return result
