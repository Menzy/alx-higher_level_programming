#!/usr/bin/python3

# Iterate through the ASCII values of uppercase letters in reverse order
for ascii_num in range(122, 96, -1):
    # Check if the ASCII value is odd
    if ascii_num % 2 == 1:
        # If odd, subtract 32 to convert to uppercase
        ascii_num = ascii_num - 32

    # Print the current character (either as is or converted to uppercase)
    print("{:c}".format(ascii_num), end='')
