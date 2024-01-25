#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # to create a new dictionary with values multiplied by 2
    n_dic = {key: value * 2 for key, value in a_dictionary.items()}

    # Return the new dictionary
    return n_dic
