#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints all integers of a list, one integer per line.

    Parameters:
        my_list (list): The input list containing integers.
    """
    for num in range(len(my_list)):
        # Print each integer using the index
        print("{:d}".format(my_list[num]))
