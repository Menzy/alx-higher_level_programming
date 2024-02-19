#!/usr/bin/python3
"""the square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square class."""

    def __init__(self, size):
        """Constructor for square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer.
        """
        self.integer_validator("size", size)
        """ Validate size as a positive integer """

        super().__init__(size, size)
        """Initialize the square as a rectangle with equal width and height"""

        self.__size = size
        """Set the size of the square"""

    def area(self):
        """Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2  # Calculate the area of the square
