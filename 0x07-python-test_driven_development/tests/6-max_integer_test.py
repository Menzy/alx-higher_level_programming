#!/usr/bin/python3
"""This module contains unit tests for the max_integer function in your_module."""

import unittest
from your_module import max_integer


class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, "Empty list should return None")

    def test_single_element_list(self):
        result = max_integer([5])
        self.assertEqual(result, 5, "Single element list should return the element itself")

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5, "List of positive numbers should return the maximum")

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1, "List of negative numbers should return the maximum")

    def test_mixed_numbers(self):
        result = max_integer([-5, 0, 10, -2, 7])
        self.assertEqual(result, 10, "List of mixed positive and negative numbers should return the maximum")

    def test_duplicate_numbers(self):
        result = max_integer([3, 2, 5, 2, 5])
        self.assertEqual(result, 5, "List with duplicate numbers should return the maximum")


if __name__ == '__main__':
    unittest.main()
