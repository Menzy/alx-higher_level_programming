#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints the elements of a list in a reversed order.

    Parameters:
        my_list (list): The input list of integers.
    """
    # Check if the input is a list
    if type(my_list) is not list:
        pass  # Do nothing if it's not a list
    else:
        # Reverse the list and print each element
        my_list.reverse()
        for item in my_list:
            print("{:d}".format(item))
