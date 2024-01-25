#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Iterate over the sorted key-value pairs of the dictionary
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
