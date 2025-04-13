#!/usr/bin/python3
"""Module that defines the BaseGeometry clas"""


class BaseGeometry:
    """Class for geometry operations"""

    def area(self):
        """Raise an exception for unimplemented area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer
        Raise TypeError or ValueError if invalid
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
