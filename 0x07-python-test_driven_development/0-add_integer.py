#!/usr/bin/python3
"""This module defines a function to add two integers or floats."""


def add_integer(a, b=98):
    """Adds two numbers, converting them to integers if they are floats."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both parameters must be integers or floats.")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
