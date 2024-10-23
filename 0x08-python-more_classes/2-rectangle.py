#!/usr/bin/python3
"""
This is the "Rectangle" module.

This module provides a simple Rectangle class with attributes for width and height.
It also includes methods to calculate the area and perimeter of the rectangle.
"""


class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle, ensuring it is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle, ensuring it is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of the rectangle (width * height)."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        Perimeter is calculated as 2 * (width + height).
        If either width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

