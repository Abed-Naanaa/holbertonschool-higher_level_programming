#!/usr/bin/python3
"""
This module generates Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        row = [1]  # First element in each row is 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element in each row is 1
        triangle.append(row)

    return triangle
