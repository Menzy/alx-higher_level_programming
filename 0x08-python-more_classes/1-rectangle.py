#!/usr/bin/python3
"""rectangle class documentation"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value: int):
        """
        Sets the width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be non-negative.")
        self.__width = value

    @property
    def height(self) -> int:
        """Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value: int):
        """
        Sets the height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be non-negative.")
        self.__height = value
