#!/usr/bin/python3
for tens_digit in range(10):
    for units_digit in range(tens_digit + 1, 10):
        print("{:d}{:d}".format(tens_digit, units_digit), end=', ' if (tens_digit, units_digit) != (9, 8) else '\n')