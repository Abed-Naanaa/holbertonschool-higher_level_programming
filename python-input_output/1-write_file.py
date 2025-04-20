#!/usr/bin/python3
"""
This module provides a function to write a string
to a UTF-8 text file and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and

    Args:
        filename (str): The name of the file
        text (str): The string to write.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)

