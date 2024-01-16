#!/usr/bin/python3

# Outer loop for the first digit in each row
for i in range(0, 9):
    # Inner loop for the second digit in each row
    for j in range(i + 1, 10):
        # Print the first digit
        print("{:d}".format(i), end='')

        # Check if it's the last pair (i=8, j=9)
        if i == 8 and j == 9:
            # If last pair, print the second digit with newline
            print("{:d}".format(j), end='\n')
        else:
            # If not the last pair, print the second digit with a comma and space
            print("{:d}".format(j), end=', ')
