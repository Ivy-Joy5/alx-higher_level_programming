#!/usr/bin/python3
class Square:
    """Represents a square."""
    
    def __init__(self, size=0):
        """Initialize the square with size."""
        self.size = size  # Using the setter to check the size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.
        
        Args:
            value (int): The size to set for the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Set the size if everything is OK

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

