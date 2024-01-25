#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Convert the list to a set to remove duplicates
    unique_set = set(my_list)

    # Convert the set back to a list and calculate the sum
    sum_of_unique = sum(list(unique_set))

    return sum_of_unique
