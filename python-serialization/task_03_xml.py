#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML format and saves it to a file.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The name of the file where the XML will be saved.
    """
    # Create the root element
    root = ET.Element("data")

    # Iterate over dictionary and create child elements
    for key, value in dictionary.items():
        # Create a child element for each key-value pair
        child = ET.SubElement(root, key)
        child.text = str(value)  # Set the text of the element to the string representation of the value

    # Create an ElementTree object and write it to a file
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file and returns it as a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Initialize an empty dictionary
        result = {}

        # Iterate over child elements and add them to the dictionary
        for child in root:
            result[child.tag] = child.text

        return result

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
