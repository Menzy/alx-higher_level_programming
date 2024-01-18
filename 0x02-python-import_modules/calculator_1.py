#!/usr/bin/python3
def add(a, b):
    """
    Function to add two numbers.

    Parameters:
    - a (int): The first number.
    - b (int): The second number.

    Returns:
    int: The sum of the two input numbers.
    """
    return a + b


def subtract(a, b):
    """
    Function to subtract two numbers.

    Parameters:
    - a (int): The first number.
    - b (int): The second number.

    Returns:
    int: The result of subtracting the second number from the first.
    """
    return a - b


def multiply(a, b):
    """
    Function to multiply two numbers.

    Parameters:
    - a (int): The first number.
    - b (int): The second number.

    Returns:
    int: The product of the two input numbers.
    """
    return a * b


def divide(a, b):
    """
    Function to divide two numbers.

    Parameters:
    - a (int): The numerator.
    - b (int): The denominator.

    Returns:
    float: The result of dividing the numerator by the denominator.
    """
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero.")
