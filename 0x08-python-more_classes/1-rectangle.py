#!/usr/bin/python3

class Rectangle:
    """This class defines a rectangle."""

    def __init__(self, width=0, height=0):
        """This function starts the rectangle with width and height."""
        self.width = width  # Use the setter to set width
        self.height = height  # Use the setter to set height

    @property
    def width(self):
        """This function retrieves (gets) the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """This function sets the width with rules."""
        if not isinstance(value, int):  # Check if width is a whole number
            raise TypeError("width must be an integer")
        if value < 0:  # Check if width is less than 0
            raise ValueError("width must be >= 0")
        self.__width = value  # Set the width if it's a good value

    @property
    def height(self):
        """This function retrieves (gets) the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """This function sets the height with rules."""
        if not isinstance(value, int):  # Check if height is a whole number
            raise TypeError("height must be an integer")
        if value < 0:  # Check if height is less than 0
            raise ValueError("height must be >= 0")
        self.__height = value  # Set the height if it's a good value

