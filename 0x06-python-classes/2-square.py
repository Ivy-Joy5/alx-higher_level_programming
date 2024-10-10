#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with a private size attribute.
        
        Args:
            size (int): The size of the square, must be a non-negative integer.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private attribute to store the size
