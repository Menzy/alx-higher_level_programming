#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # Use dictionary comprehension to create a new dictionary
    # excluding key-value pairs with the specified value
    updated_dictionary = {
        key: val for key, val in a_dictionary.items() if val != value
    }

    return updated_dictionary
