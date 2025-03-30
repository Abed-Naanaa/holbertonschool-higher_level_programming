#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = ""
    for char in text:
        result += char
        if char in ".:?":
            result += "\n\n"

    lines = [line.strip() for line in result.split("\n")]
    print("\n".join(lines))
