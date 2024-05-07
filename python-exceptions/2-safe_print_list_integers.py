#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # Initialize counter for the number of integers printed
    count = 0
    # Iterate over the list up to the specified number of elements or the end of the list
    for i in range(x):
        try:
            # Attempt to format the element as an integer
            print("{:d}".format(my_list[i]), end="")
            # If successful, increment the counter
            count += 1
        except (ValueError, TypeError):
            # If a ValueError or TypeError is raised, skip the element silently
            pass
        except IndexError:
            # If an IndexError is raised (meaning we've reached the end of the list), 
            # instead of breaking, raise the exception to trigger the traceback
            raise
    # Print a newline to ensure the output is properly formatted
    print()
    # Return the actual number of integers printed
    return count