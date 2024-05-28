#!/usr/bin/python3

"""Defines unittests for models/rectangle.py."""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0 # Reset the number of objects before each test

    def test_instance_creation(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

    def test_instance_creation_with_args(self):
        r2 = Rectangle(10, 2, 1, 1, 99)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.id, 99)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "1")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -1)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_display(self):
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_method(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=89)
        self.assertEqual(r1.id, 89)
        r1.update(width=2, height=3, x=4, y=5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dict = r1.to_dictionary()
        expected_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1_dict, expected_dict)
        self.assertIsInstance(r1_dict, dict)

if __name__ == "__main__":
    unittest.main()