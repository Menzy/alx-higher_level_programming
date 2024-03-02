#!/usr/bin/python3
"""Unittest for the Base class"""


import unittest
import inspect
import json
from models import base
from models.base import Base


class TestBaseDocstrings(unittest.TestCase):
    """unittest class for the Base class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_module_doc(self):
        """Test documentation"""

        self.assertTrue(len(base.__doc__) > 0)

    def test_func_docstrings(self):
        """Tests for the existence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) > 0)


class TestBase(unittest.TestCase):
    """Tests to check functionality of Base class"""
    def test_too_many_args(self):
        """test too many args to init - class constructor"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_no_id(self):
        """Test when no id is passed(default as None)"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_nb_private(self):
        """Tests nb_objects as a private instance attribute"""
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_to_json_string(self):
        """Tests regular to json string"""
        Base._Base__nb_objects = 0
        dict1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        dict2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_str = Base.to_json_string([dict1, dict2])
        self.assertTrue(type(json_str) is str)
        d = json.loads(json_str)
        self.assertEqual(d, [dict1, dict2])


    def test_from_json_string(self):
        """Tests regular from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_list = Base.from_json_string(json_str)
        self.assertTrue(type(json_list) is list)
        self.assertEqual(len(json_list), 2)
        self.assertTrue(type(json_list[0]) is dict)
        self.assertTrue(type(json_list[1]) is dict)
        self.assertEqual(json_list[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_list[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_from_json_string_empty(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_None(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(None))

if __name__ == '__main__':
    unittest.main()