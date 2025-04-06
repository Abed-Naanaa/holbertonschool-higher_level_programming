#!/usr/bin/python3
"""Defines a class Square with size validation and a method to print the square."""

class Square:
    """Represents a square with a validated size and prints the square.

    The size is validated to be an integer and greater than or equal to 0.
    The class includes a method to print the square using the '#' character.
    """

    def __init__(self, size=0):
        """Initializes the square with a given size and validates it.

        Args:
            size (int): The size of the square, default is 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square and validates it.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
