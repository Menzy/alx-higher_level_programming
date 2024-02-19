#!/usr/bin/python3
"""function to check if an object is a subclass of a specified class."""


def inherits_from(obj, a_class):
    """Checks if an object is a subclass of a specified class.

    Parameters:
        obj: Any Python object
        a_class: The class to compare the object against

    Returns:
        True if the object is a subclass of specified class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
