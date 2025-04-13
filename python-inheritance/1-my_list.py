#!/usr/bin/python3
"""
Module containing a class MyList that inherits from list.
This class adds a method `print_sorted` to prin.
"""

class MyList(list):
    """
    MyList class that inherits from the built-in list class.
    It adds a method `print_sorted` to print the lis.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
