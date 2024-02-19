#!/usr/bin/python3
"""function to check if an object is an instance of a specified class."""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of or an instance of a class that \
        inherited from a specified class.

    Parameters:
        obj: Any Python object
        a_class: The class to compare the object against

    Returns:
        True if the object is an instance of the specified class or its \
            subclasses, otherwise False.
    """
    return isinstance(obj, a_class)
