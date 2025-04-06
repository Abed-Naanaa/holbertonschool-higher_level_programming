#!/usr/bin/python3
"""Defines a class Square with size and position validation and a method to print the square."""

class Square:
    """Represents a square with a validated size and position, and prints the square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with a given size and position, validating both.
        
        Args:
            size (int): The size of the square, default is 0.
            position (tuple): The position of the square, default is (0, 0).
        
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square and validates it.

        Args:
            value (tuple): The position of the square (x, y).

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #, considering the position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()  # Print spaces for position[1]
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
