#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    # Use list comprehension to create a new list.
    return list(map(lambda i: i * number, my_list))
