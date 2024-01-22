#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Returns a new list of Boolean values indicating
    whether each element in the input list is divisible by 2.
    Returns None if the input list is empty or None.
    """
    if not my_list:
        return None

    # Create a new list with True if divisible by 2, else False
    new_list = [n % 2 == 0 for n in my_list]

    return new_list
