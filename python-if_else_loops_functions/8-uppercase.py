#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122: # ASCII values for 'a' to 'z'
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print("{:c}".format(ord(char)), end="")
    print()
