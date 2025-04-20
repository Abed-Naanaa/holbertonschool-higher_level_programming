#!/usr/bin/python3
"""
This module defines a class Student with attributes
and a method to retrieve a filtered dictionary representation.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the instance,

        Args:
            attrs (list, optional): A list of attribute 
            
        Returns:
            dict: A dictionary with the instance attributes,
        """
        if attrs is None:
            return self.__dict__

        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)

        return filtered_dict
