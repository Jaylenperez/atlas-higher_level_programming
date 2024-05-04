#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        return
    for i, row in enumerate(matrix):
        for num in row:
            print("{:d}".format(num), end=' ')
        # Print a newline character only if it's not the last row
        if i < len(matrix) - 3:
            print()
