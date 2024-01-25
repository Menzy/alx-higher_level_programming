#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Use list comprehension to create a new list with replacements
    new_list = [replace if el == search else el for el in my_list]
    return new_list
