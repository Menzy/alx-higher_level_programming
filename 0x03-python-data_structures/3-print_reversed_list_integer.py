#!/usr/bin/python3

def print_reversed_list_integer(my_list=None):
    if my_list is None:
        my_list = []

    my_list.reverse()  # In-place reversal

    for i in my_list:
        print("{}".format(i))
