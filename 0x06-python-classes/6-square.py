#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square object.

        Args:
            size (int): The size of the square. Defaults to 0.
                Must be a non-negative integer.

            position (tuple): The position of the square. Defaults to (0, 0).
                Must be a tuple of two positive integers.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position[0], int)) or \
                (not isinstance(position[1], int)) or \
                (position[0] < 0) or (position[1] < 0) or \
                (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: The position of the square as a tuple of two integers.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value[0], int)) or \
                (not isinstance(value[1], int)) or \
                (value[0] < 0) or (value[1] < 0) or \
                (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
