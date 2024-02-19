#!/usr/bin/python3
"""function to check if an object is an instance of a specified class."""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class.

    Parameters:
        obj: Any Python object
        a_class: The class to compare the object against

    Returns:
        True if the object is an instance, otherwise False.
    """
    if type(obj) is a_class:
        return True
    
    else:
        return False
