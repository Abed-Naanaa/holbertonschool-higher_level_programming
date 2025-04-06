#!/usr/bin/python3
"""Defines a class Square with a private size attribute."""


class Square:
    """Represents a square by its size.

    The class has a private instance attribute
    the square with a given size.
    """

    def __init__(self, size=0):
        """Initializes the square with a given size.

        Args:
            size (int): The size of the square, default is 0.
        """
        self.__size = size
