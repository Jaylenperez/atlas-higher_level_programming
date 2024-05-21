#!/usr/bin/python3
"""This module defines a class Student"""

# Define a class named Student to represent a student.
class Student:
    """Represent a student."""

    # Constructor method (__init__) for initializing a new Student instance.
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student"""
        
        # Assign the first_name, last_name, and age attributes to the instance.
        # These attributes store the personal details of the student.
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Method to get a dictionary representation of the Student instance.
    def to_json(self):
        """Gets a dictionary representation of the Student"""
        
        # Return the __dict__ attribute of the instance, which contains the instance's attributes and their values.
        # This effectively gives us a dictionary representation of the student's state.
        return self.__dict__
