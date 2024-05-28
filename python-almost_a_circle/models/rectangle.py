#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base # Import the Base class from the models.base module.

class Rectangle(Base): # Create Rectangle class that inherits from Base class
    """
    Represents a rectangle with properties such as width, height, x, y, and id.
    Inherits from the Base class to utilize its unique ID assignment feature.
    """

    def __init__(self, width, height, x=0, y=0, id=None): # Constructor initializing rectangle with dimensions and position
        """
        Initializes a new Rectangle instance with given dimensions and position.
        
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-cooddinate of the rectangle. Defaults to 0.
            y (int, optional): Y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): Unique ID for the rectangle. Defaults to None.
        """
        super().__init__(id) # Call parent class constructor to initialize ID

        self.width = width # Set width of rectangle
        self.height = height # Set height of rectangle
        self.x = x # Set x-coordinate of rectangle
        self.y = y # Set y-coordinate of rectangle

    @property # Property getter for the width property
    def width(self):
        """
        Getter for the width property.
        """
        return self.__width

    @width.setter # Property setter for the width property
    def width(self, value):
        """
        Setter for the width property.
        
        Args:
            value (int): New width value.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int): # Ensure value is an integer
            raise TypeError("width must be an integer")
        if value <= 0: # Width must be positive
            raise ValueError("width must be > 0")
        self.__width = value # Update width

    @property # Property getter for height property
    def height(self):
        """
        Getter for the height property.
        """
        return self.__height

    @height.setter # Property setter for height property
    def height(self, value):
        """
        Setter for the height property.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int): # Ensure height is an integer
            raise TypeError("height must be an integer")
        if value <= 0: # height must be positive
            raise ValueError("height must be > 0")
        self.__height = value # Update height

    @property # Property getter for x-coordinate property.
    def x(self):
        """
        Getter for the x-coordinate property.
        """
        return self.__x

    @x.setter # Property setter for x-coordinate property.
    def x(self, value):
        """
        Setter for the x-coordinate property.
        
        Args:
            value (int): New x-coordinate value.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int): # Ensure that value is an integer
            raise TypeError("x must be an integer")
        if value < 0: # x must be positive
            raise ValueError("x must be >= 0")
        self.__x = value # Update x

    @property # Property getter for the y-coordinate property.
    def y(self):
        """
        Getter for the y-coordinate property.
        """
        return self.__y

    @y.setter # Property setter for the y-coordinate property.
    def y(self, value):
        """
        Setter for the y-coordinate property.

        Args: 
            value (int): New y-coordinate value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int): # Ensure value is an integer
            raise TypeError("y must be an integer")
        if value < 0: # y must be positive
            raise ValueError("y must be >= 0")
        self.__y = value # Update y

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        area = self.width * self.height # The width represents one side of the rectangle. It is multiplied by the height attribute (the other side) to calculate the total area.

        return area # Calculated area is returned to the caller.

    def display(self):
        """
        Prints the rectangle to the console.
        """
        for _ in range(self.y): # Loop through y-coordinate of rectangle, printing empty lines to create space above the rectangle
            print()

        for _ in range(self.height): # Loop over the height of the rectangle
            print(" " * self.x + "#" * self.width) # Print spaces equal to the x-coordinate followed by '#' characters equal to the width

    def __str__(self):
        """
        Returns a string representation of the rectangle instance.

        Returns:
            str: Formatted string representation of the rectangle.
        """
        # Returns a formatted string that includes the class name "Rectangle" followed by its attrubutes (id, x, y, width, height)
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, # Inserts id attribute of the instance
                                                       self.x,  # Inserts x coordinate of the instance
                                                       self.y,  # Inserts y coordinate of the instance
                                                       self.width, # Inserts the width of the instance
                                                       self.height) # Inserts the height of the instance

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle instance.

        Args:
            *args: Positional arguments specifying the attributes to update in order: id, width, height, x, y.
            **kwargs: Keyword arguments specifying the attributes to update.
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

        elif len(kwargs) > 0: # Checking if keyword arguments were passed
            for key, value in kwargs.items():
                if key == "id": # Assigning the id attribute of the instance
                    self.id = value
                elif key == "width": # Assigning the width attribute of the instance
                    self.width = value
                elif key =="height": # Assigning the height attribute of the instance
                    self.height = value
                elif key == "x": # Assigning the x attribute of the instance
                    self.x = value
                elif key == "y": # Assigning the y attribute of the instance
                    self.y = value
                else:
                    break
    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle instance.

        Returns:
            dict: Dictionary representation of the rectangle instance.
        """
        rec_dict = { # Creating dictionary with the rectangle instance's attributes
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }

        return rec_dict
