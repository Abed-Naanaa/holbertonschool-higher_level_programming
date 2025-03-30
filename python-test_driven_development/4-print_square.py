#!/usr/bin/python3
"""Module for printing a square with the character '#'."""

def print_square(size):
    """Prints a square with the character '#' of given size.
    
    Args:
        size: The length of the square's sides. Must be a non-negative integer.
    
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print('#' * size)
