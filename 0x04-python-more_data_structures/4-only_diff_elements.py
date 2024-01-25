#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Calculate the symmetric difference of set_1 and set_2
    set_diff = set_1 ^ set_2

    # Return the set of elements that are only in one of the sets
    return set_diff
