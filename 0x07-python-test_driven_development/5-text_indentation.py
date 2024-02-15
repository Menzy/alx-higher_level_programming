#!/usr/bin/python3

"""a function to format text by adding new lines after certain characters."""


def text_indentation(text):
    """
    Prints a text with two new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to be processed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    lines = text.splitlines()

    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace
        if line:  # Skip empty lines
            for char in line:
                print(char, end='')
                if char in punctuations:
                    print('\n\n', end='')
            print()
