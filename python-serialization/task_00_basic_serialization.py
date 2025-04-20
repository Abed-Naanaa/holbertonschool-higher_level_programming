#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    
    Args:
        data (dict): A Python dictionary to serialize.
        filename (str): The filename where the serialized data will be saved.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Data serialized and saved to '{filename}'.")

def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file into a Python dictionary.
    
    Args:
        filename (str): The filename containing the JSON data.
    
    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
