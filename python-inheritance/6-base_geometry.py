#!/usr/bin/python3
"""Module that defines the BaseGeometry class"""


class BaseGeometry:
    """Class for geometry operations"""

    def area(self):
        """Raise an exception for unimplemented area method"""
        raise Exception("area() is not implemented")
