#!/usr/bin/python3
"""Module for text indentation with specific characters."""

def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':' characters.
    
    Args:
        text: A string to process and print with the required indentations.
    
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = ['.', '?', ':']
    new_text = ""
    for char in text:
        new_text += char
        if char in chars:
            new_text += "\n\n"
    print(new_text.strip())
