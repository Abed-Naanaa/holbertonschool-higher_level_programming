#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file.
        
        Args:
            filename (str): The name of the file
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            print(f"Object serialized and saved to '{filename}'.")
        except Exception as e:
            print(f"Error serializing the object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from th
        
        Args:
            filename (str): The name of the file to
        
        Returns:
            CustomObject: The deserialized object, or None
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error deserializing the object: {e}")
            return None
