#!/usr/bin/python3

def print_last_digit(number):
    # If the number is negative, take its absolute value
    if number < 0:
        number = -number
    
    # Print the last digit of the absolute value of the number
    print("{:d}".format(number % 10), end='')

    # Return the last digit
    return number % 10
