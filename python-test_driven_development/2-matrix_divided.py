#!/usr/bin/python3
"""Module for dividing all elements of a matrix."""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.
    
    Args:
        matrix: A list of lists containing integers or floats.
        div: The number by which to divide the matrix elements (must be int or float).
    
    Returns:
        A new matrix with each element divided by div, rounded to 2 decimal places.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or 
        not all(isinstance(row, list) for row in matrix) or 
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0]) if matrix else 0
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(num / div, 2) for num in row] for row in matrix]
