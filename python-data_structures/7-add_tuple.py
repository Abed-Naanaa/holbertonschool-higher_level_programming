#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements, padding with 0s if needed
    a1, a2 = tuple_a + (0, 0)
    b1, b2 = tuple_b + (0, 0)
    
    # Add corresponding elements and return the result
    return (a1 + b1, a2 + b2)
