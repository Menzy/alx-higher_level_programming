#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the element at the specified index in the given list.

    Parameters:
        my_list (list): The input list.
        idx (int): The index at which to delete the element.

    Returns:
        list: The modified list after deletion.
    """
    if my_list is not None and 0 <= idx < len(my_list):
        # Check if the index is valid and delete the element
        del my_list[idx]

    return my_list
