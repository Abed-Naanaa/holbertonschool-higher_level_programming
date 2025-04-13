#!/usr/bin/python3
"""Module that defines a class MyList inheriting from list"""


class MyList(list):
    """A class that inherits from list and prints it sorted"""

    def print_sorted(self):
        """Print the list in ascending sorted order"""
        print(sorted(self))
