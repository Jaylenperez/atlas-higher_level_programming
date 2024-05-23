#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle # Imports the Rectangle class from the models.rectangle module.

if __name__ == "__main__": # Ensures code runs only when the script is executed directly (not when imported as module)

    r1 = Rectangle(10, 2) # Creates 3 instances of Rectangle class with different arguments
    print(r1.id) # Print the id attribute of each instance

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
