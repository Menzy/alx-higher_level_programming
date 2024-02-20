#!/usr/bin/python3
"""read from a file"""


def read_file(filename=""):
    """a function that reads a text file and prints it to stdout"""

    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end="")
