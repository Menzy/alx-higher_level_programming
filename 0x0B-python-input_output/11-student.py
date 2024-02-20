#!/usr/bin/python3
"""
a class Student that defines a student
"""


class Student:
    """
    This is the student class
    """

    def __init__(self, first_name, last_name, age):
        """
        INitializes a student instance
        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs:
                A list of attribute names to be retrieved.
                If not provided or None, all attributes are
                retrieved.

        Returns:
            dict: A dictionary representation of the Student instance.
                If attrs is provided, only the specified attributes
                are included.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)
        return filtered_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Args:
            json:
                A dictionary representing the attributes of the
                Student instance.
                The dictionary keys are the attribute names, and
                the values are the attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
