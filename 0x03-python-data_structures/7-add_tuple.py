#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds the first two elements of two tuples and returns the
    result as a new tuple.
    """
    # Extract the first two elements from each tuple
    a = tuple_a[:2]
    b = tuple_b[:2]

    # Calculate the element-wise sum
    result = tuple(x + y for x, y in zip(a, b))

    return result
