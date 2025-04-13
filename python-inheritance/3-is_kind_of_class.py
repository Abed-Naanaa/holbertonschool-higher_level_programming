#!/usr/bin/python3
"""Module that checks if an object is an instance or"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or inherits"""
    return isinstance(obj, a_class)
