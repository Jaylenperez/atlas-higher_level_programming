#!/usr/bin/python3

"""Defines unittests for models/square.py."""

import io
import sys
import unittest
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0 # Reset the number of objects before each test

    def test_instance_creation(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

    def test_instance_creation_with_args(self):
        s2 = Square(7, 2, 3, 10)
        self.assertEqual(s2.size, 7)
        self.assertEqual(s2.width, 7)
        self.assertEqual(s2.height, 7)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 10)

    def test_size_validation(self):
        with self.assertRaises(TypeError):
            Square("10")
        with self.assertRaises(ValueError):
            Square(-10)
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            Square(10, "1")
        with self.assertRaises(ValueError):
            Square(10, -1)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            Square(10, 1, "1")
        with self.assertRaises(ValueError):
            Square(10, 1, -1)

    def test_area(self):
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_display(self):
        s1 = Square(2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_method(self):
        s1 = Square(3, 1, 2, 50)
        self.assertEqual(str(s1), "[Square] (50) 1/2 - 3")

    def test_update_args(self):
        s1 = Square(5)
        s1.update(89)
        self.assertEqual(s1.id, 89)
        s1.update(89, 2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        s1.update(89, 2, 3)
        self.assertEqual(s1.x, 3)
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.y, 4)

    def test_update_kwargs(self):
        s1 = Square(5)
        s1.update(id=89)
        self.assertEqual(s1.id, 89)
        s1.update(size=2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        s1.update(x=3)
        self.assertEqual(s1.x, 3)
        s1.update(y=4)
        self.assertEqual(s1.y, 4)

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 1)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1_dict, expected_dict)
        self.assertIsInstance(s1_dict, dict)

if __name__ == "__main__":
    unittest.main()