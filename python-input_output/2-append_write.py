#!/usr/bin/python3
"""
This module provides a function to append a string
to a UTF-8 text file and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 text file

    Args:
        filename (str): The name of the file to append to
        text (str): The string to append.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
