#!/usr/bin/python3
"""This module defines the Square class."""


# Define the Square class
class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initialize the Square object.

         Args:
            size (int): size of the square (defaults to 0 if not provided).
                Must be an integer not less than 0."""

        # Set the size of the square
        self.__size = size

    def area(self):
        """Calculates and returns the area of a square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with character #"""

        # Check if the size is 0, then print an empty line
        if self.__size == 0:
            print()
        else:
            # Iterate through rows of the square
            for i in range(self.__size):
                # Iterate through columns of the square
                for j in range(self.__size):
                    # Print '#' character without newline
                    print('#', end='')
                # Move to the next line after printing a row
                print()

    @property
    def size(self):
        """Retrieves private instance attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets private instance attribute.

         Raises:
            TypeError - when size passed is not an integer.
            ValueError - when size is less than 0."""

        # Validate the new size value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        # Set the new size value
        self.__size = value
