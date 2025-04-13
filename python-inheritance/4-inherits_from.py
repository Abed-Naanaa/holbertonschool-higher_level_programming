#!/usr/bin/python3
"""Module that checks for inherited instances of a class"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class,
    but not if it is exactly an instance of a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
