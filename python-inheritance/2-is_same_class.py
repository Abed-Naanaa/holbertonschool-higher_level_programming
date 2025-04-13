#!/usr/bin/python3
"""Module that defines a function to check object class equality"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly"""
    return type(obj) is a_class
