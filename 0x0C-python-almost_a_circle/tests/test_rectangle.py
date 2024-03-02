#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_init_with_id(self):
        rectangle = Rectangle(2, 3, 1, 1, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 1)
        self.assertEqual(rectangle.id, 1)

    def test_rectangle_init_without_id(self):
        rectangle = Rectangle(2, 3, 1, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 1)
        self.assertEqual(rectangle.id, 1)

    def test_rectangle_init_with_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 3, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle("2", 3, 1, 1)

    def test_rectangle_init_with_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 0, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(2, "3", 1, 1)

    def test_rectangle_init_with_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -1, 1)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, "1", 1)

    def test_rectangle_init_with_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 3, 1, -1)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 1, "1")

    def test_rectangle_area(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.area(), 6)

    def test_rectangle_display(self):
        rectangle = Rectangle(2, 3)
        expected_output = "##\n" \
                          "##\n" \
                          "##\n"
        with unittest.mock.patch('builtins.print') as mock_print:
            rectangle.display()
            mock_print.assert_called_once_with(expected_output)

    def test_rectangle_to_dictionary(self):
        rectangle = Rectangle(2, 3, 1, 1, 1)
        expected_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 1, 'y': 1}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
