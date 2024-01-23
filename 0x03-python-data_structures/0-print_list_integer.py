#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints each integer in the provided list.

    Parameters:
        my_list (list): List of integers to be printed
    """
    for num in my_list:
        print("{:d}".format(num))
