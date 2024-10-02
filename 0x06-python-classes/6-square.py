#!/usr/bin/python3
class Square:
    """Represents a square with a size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with an optional size and position."""
        self.size = size
        self.position = position

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
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position of the square.
        
        Args:
            value (tuple): The position to set for the square.
        
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #.
        
        If size is 0, print an empty line.
        Position is used to print the square with spaces.
        """
        if self.__size == 0:
            print("")
            return

        # Print the new lines for the position[1]
        for _ in range(self.__position[1]):
            print("")

        # Print the square with spaces based on position[0]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

