#!/usr/bin/python3
"""This module defines a function to print a square."""


def print_square(size):
    """Prints a square using the '#' character."""
    if not isinstance(size, int):
        if isinstance(size, float) and size.is_integer():
            size = int(size)
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
