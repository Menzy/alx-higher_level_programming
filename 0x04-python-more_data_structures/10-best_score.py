#!/usr/bin/python3

def best_score(a_dictionary):
    # Check if the dictionary is empty or None
    if not a_dictionary:
        return None

    # Use max function to find the key with the maximum value
    return max(a_dictionary, key=lambda key: a_dictionary[key])
