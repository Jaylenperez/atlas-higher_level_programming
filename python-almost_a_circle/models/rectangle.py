#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base # Import the Base class from the models.base module.

class Rectangle(Base): # Create Rectangle class that inherits from Base class
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None): # Constructor initializing rectangle with dimensions and position
        super().__init__(id) # Call parent class constructor to initialize ID

        self.width = width # Set width of rectangle
        self.height = height # Set height of rectangle
        self.x = x # Set x-coordinate of rectangle
        self.y = y # Set y-coordinate of rectangle

    @property # Property methods and setters are used to encapsulate access to the private instance variables.
    def width(self):
        """Gets the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int): # Ensure value is an integer
            raise TypeError("width must be an integer")
        if value <= 0: # Width must be positive
            raise ValueError("width must be > 0")
        self.__width = value # Update width

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int): # Ensure height is an integer
            raise TypeError("height must be an integer")
        if value <= 0: # height must be positive
            raise ValueError("height must be > 0")
        self.__height = value # Update height

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int): # Ensure that value is an integer
            raise TypeError("x must be an integer")
        if value < 0: # x must be positive
            raise ValueError("x must be >= 0")
        self.__x = value # Update x

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int): # Ensure value is an integer
            raise TypeError("y must be an integer")
        if value < 0: # y must be positive
            raise ValueError("y must be >= 0")
        self.__y = value # Update y

    def area(self):
        """
        This method calculates and returns the area of the rectangle.
        """
        area = self.width * self.height # The width represents one side of the rectangle. It is multiplied by the height attribute (the other side) to calculate the total area.

        return area # Calculated area is returned to the caller.

    def display(self):
        """
        Prints the size of rectangle using #
        """
        for _ in range(self.y): # Loop through y-coordinate of rectangle, printing empty lines to create space above the rectangle
            print()

        for _ in range(self.height): # Loop over the height of the rectangle
            print(" " * self.x + "#" * self.width) # Print spaces equal to the x-coordinate followed by '#' characters equal to the width

    def __str__(self):
        """
        Defines a format for the string representation of the class"""
        # Returns a formatted string that includes the class name "Rectangle" followed by its attrubutes (id, x, y, width, height)
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, # Inserts id attribute of the instance
                                                       self.x,  # Inserts x coordinate of the instance
                                                       self.y,  # Inserts y coordinate of the instance
                                                       self.width, # Inserts the width of the instance
                                                       self.height) # Inserts the height of the instance

    def update(self, *args, **kwargs):
        """
        Assign arguments to attributes based on their positions.
        """
        if args: # Checks if any positional arguments were passed to the method.
            attributes = ["id", "width", "height", "x", "y"] # Initialize list of attribute names in the order they should be assigned

            for count, arg in enumerate(args): # Iterates over the positional arguments passed to the method
                if count == 0: # Assigns the 1st argument to the id attribute of the instance
                    self.id = arg
                elif count == 1: # Assings the 2nd argument to the width attribute of the instance
                    self.width = arg
                elif count == 2: # Assigns the 3rd argument to the height attribute of the instance
                    self.height = arg
                elif count == 3: # Assigns the 4th argument to the x attribute of the instance
                    self.x = arg
                elif count == 4: # Assings the 5th argument to the y attribute of the instance
                    self.y = arg
                else: # Exits the loop if more than 5 arguments are passed, as there are no more attributes to assign
                    break