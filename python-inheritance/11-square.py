#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a square with validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
