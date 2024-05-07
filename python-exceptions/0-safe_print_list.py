#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize counter
    count = 0
    # Use a try/except block to handle errors
    try:
        # Iterate over the list up to the specified number of elements or the end of the list
        for i in range(x):
            # Print the element, followed by a space
            print(my_list[i], end='')
            # Increment the counter
            count += 1
    except IndexError:
        # If IndexError occurs
        # print a newline to end of file
        print()
        return count
    # Print a newline to ensure the output is properly formatted
    print()
    # Return the actual number of elements printed
    return count