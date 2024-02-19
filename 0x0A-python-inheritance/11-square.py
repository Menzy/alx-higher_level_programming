#!/usr/bin/python3
"""the Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square class"""

    def __init__(self, size):
        """Constructor for the size instance"""
        if not isinstance(size, (int, float)):
            raise TypeError("size must be an integer or a float")
        if size <= 0:
            raise ValueError("size must be > 0")
        super().__init__(size, size)
        """Initialize width and height of the square"""

        self.__size = size  # Set the size of the square

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square object"""
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """Returns the representation of the square object"""
        return f"Square({self.__size})"
