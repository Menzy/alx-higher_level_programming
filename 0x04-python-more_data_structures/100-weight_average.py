#!/usr/bin/python3

def weight_average(my_list=[]):
    # Check if the input list is empty
    if my_list == []:
        return 0

    sum_weighted_values, sum_weights = 0, 0

    # Iterate through each tuple in the list
    for weight, value in my_list:
        # Calculate the weighted sum of values
        sum_weighted_values += weight * value
        # Calculate the sum of weights
        sum_weights += weight

    # Calculate the weighted average (avoid division by zero)
    if sum_weights != 0:
        weighted_avg = sum_weighted_values / sum_weights
    else:
        weighted_avg = 0

    return weighted_avg
