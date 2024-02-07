#!/usr/bin/python3
"""This module defines the Square class."""


# Define the Square class
class Square:
    """This class defines a square."""

    # Constructor method to initialize square objects
    def __init__(self, size=0):
        """Initialize the Square object.

         Args:
            size (int): size of the square (defaults to 0 if not provided).
                Must be an integer not less than 0.

        Raises:
            TypeError: when size passed is not an integer.
            ValueError: when size is less than 0."""

        # Validate the size argument
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        # Assign the size to the instance attribute
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size
