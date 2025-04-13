#!/usr/bin/python3
"""Module that defines the BaseGeometry class with area and integer validation

>>> bg = BaseGeometry()
>>> bg.area()
Traceback (most recent call last):
    ...
Exception: area() is not implemented

>>> bg.integer_validator("width", 5)
>>> bg.integer_validator("height", -5)
Traceback (most recent call last):
    ...
ValueError: height must be greater than 0

>>> bg.integer_validator("name", "John")
Traceback (most recent call last):
    ...
TypeError: name must be an integer
"""


class BaseGeometry:
    """Class for geometry operations"""

    def area(self):
        """Raise an exception for unimplemented area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer
        Raise TypeError or ValueError if invalid

        >>> bg = BaseGeometry()
        >>> bg.integer_validator("width", 5)
        >>> bg.integer_validator("height", "10")
        Traceback (most recent call last):
            ...
        TypeError: height must be an integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
