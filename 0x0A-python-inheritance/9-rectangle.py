#!/usr/bin/python3
"""Defines the BaseGeometry and Rectangle classes."""


class BaseGeometry:
    """Creates the BaseGeometry class."""

    def area(self):
        """Calculates the area. Raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The integer value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Creates the Rectangle class, a subclass of BaseGeometry."""

    def __init__(self, width, height):
        """Instantiates a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
