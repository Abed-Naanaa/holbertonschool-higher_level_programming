#!/usr/bin/python3
"""
This module defines a class Student with attributes
and methods to serialize and deserialize its data.
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
        Returns the dictionary representation of the instance

        Args:
            attrs (list, optional): A list of attribute nam
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary with keys as attribute names
        """
        for key, value in json.items():
            setattr(self, key, value)
