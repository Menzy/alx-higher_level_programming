#!/usr/bin/python3

def magic_calculation(a, b, c):
    # Check if a is less than b
    if a < b:
        # If true, return the value of c
        return c
    # Check if c is greater than b
    elif c > b:
        # If true, return the sum of a and b
        return a + b
    # If neither condition is met, return the result of (a * b) - c
    else:
        return (a * b) - c
