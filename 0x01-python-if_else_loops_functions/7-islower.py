#!/usr/bin/python3

def islower(c):
    # Get the ASCII value of the character
    ascii_num = ord(c)

    # Check if the ASCII value is within the range
    if ascii_num >= 97 and ascii_num <= 122:
        return True
    else:
        return False
