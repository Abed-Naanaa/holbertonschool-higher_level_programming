#!/usr/bin/python3
"""
This module provides a function that returns the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a simple data object.

    Args:
        obj: An instance of a class with onl

    Returns:
        dict: A dictionary containing all serializable attr
    """
    return obj.__dict__
