#!/usr/bin/python3

# Loop through the range of numbers from 0 to 99
for num in range(0, 100):
    # Check if the current number is 99
    if num == 99:
        # If it's the last number, print with a newline
        print("{:02d}".format(num), end='\n')
    else:
        # If it's not the last number, print with a comma and space
        print("{:02d}".format(num), end=', ')
