#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Try to print the integer value
        print("{:d}".format(value))

        # If printing is successful, return True
        return True
    except (ValueError, TypeError):
        # If a ValueError or TypeError occurs during printing, return False
        return False
