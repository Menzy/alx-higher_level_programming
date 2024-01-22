#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Returns the maximum integer in the list.
    Returns None if the list is empty or None.
    """
    if not my_list or len(my_list) == 0:
        return None

    # Sort the list in ascending order and return the last element
    return sorted(my_list)[-1]
