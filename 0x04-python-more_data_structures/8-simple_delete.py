#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Use pop method to delete the key if it exists
    a_dictionary.pop(key, None)

    # Return the updated dictionary
    return a_dictionary
