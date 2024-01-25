#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Initialize an empty list to store common elements
    _set = []

    # Iterate through elements in set_1
    for y in set_1:
        # Iterate through elements in set_2
        for x in set_2:
            # Check if the current elements are equal (common element)
            if y == x:
                # Append the common element to the list
                _set.append(y)

    # Return the list of common elements
    return _set
