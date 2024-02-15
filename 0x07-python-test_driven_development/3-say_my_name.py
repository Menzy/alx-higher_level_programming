#!/usr/bin/python3
"""This module defines a function to print a name."""


def say_my_name(first_name, last_name=""):
    """Prints a name composed of a first name and an optional last name."""
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name or last_name must be a string")
    if last_name:
        print("My name is", first_name, last_name)
    else:
        print("My name is", first_name)
