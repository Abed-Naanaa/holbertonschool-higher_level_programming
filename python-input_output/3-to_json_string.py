#!/usr/bin/python3
"""
This module provides a function that returns
the JSON string representation of a Python object.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of an object.

    Args:
        my_obj: The Python object to convert.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)

