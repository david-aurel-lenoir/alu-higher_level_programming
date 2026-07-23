#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def setUp(self):
        """Reset the __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_two_args(self):
        """Check Rectangle(1, 2) basic instantiation."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_rectangle_three_args(self):
        """Check Rectangle(1, 2, 3) instantiation."""
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 0))

    def test_rectangle_four_args(self):
        """Check Rectangle(1, 2, 3, 4) instantiation."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_rectangle_five_args(self):
        """Check Rectangle(1, 2, 3, 4, 5) instantiation with id."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(
            (r.width, r.height, r.x, r.y, r.id), (1, 2, 3, 4, 5)
        )

    def test_width_string_type_error(self):
        """Check TypeError is raised when width is a string."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_string_type_error(self):
        """Check TypeError is raised when height is a string."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_string_type_error(self):
        """Check TypeError is raised when x is a string."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_string_type_error(self):
        """Check TypeError is raised when y is a string."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_zero_value_error(self):
        """Check ValueError is raised when width == 0."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_width_negative_value_error(self):
        """Check ValueError is raised when width < 0."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_zero_value_error(self):
        """Check ValueError is raised when height == 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_height_negative_value_error(self):
        """Check ValueError is raised when height < 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_x_negative_value_error(self):
        """Check ValueError is raised when x < 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_y_negative_value_error(self):
        """Check ValueError is raised when y < 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Check the area calculation."""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_display_basic(self):
        """Check the display() method exists and prints correctly."""
        r = Rectangle(2, 2)
        expected = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_with_position(self):
        """Check display() with x and y offsets applied."""
        r = Rectangle(2, 2, 2, 2)
        expected = "\n\n  ##\n  ##\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_str(self):
        """Check the string representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_to_dictionary(self):
        """Check to_dictionary() exists and returns correct values."""
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_independent(self):
        """Check the returned dict is independent of the instance."""
        r = Rectangle(10, 2)
        d = r.to_dictionary()
        d["width"] = 100
        self.assertEqual(r.width, 10)

    def test_update_no_args(self):
        """Check update() with no arguments does nothing."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (1, 10, 10, 10, 10))

    def test_update_one_arg(self):
        """Check update(89) updates only id."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_two_args(self):
        """Check update(89, 1) updates id and width."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_three_args(self):
        """Check update(89, 1, 2) updates id, width, height."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_four_args(self):
        """Check update(89, 1, 2, 3) updates id, width, height, x."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2, 3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_five_args(self):
        """Check update(89, 1, 2, 3, 4) updates all attributes."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (89, 1, 2, 3, 4))

    def test_update_kwargs_id(self):
        """Check update(**{'id': 89}) updates only id."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{"id": 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_width(self):
        """Check update with id and width kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{"id": 89, "width": 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_kwargs_height(self):
        """Check update with id, width and height kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_kwargs_x(self):
        """Check update with id, width, height and x kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_kwargs_full(self):
        """Check update with all attributes as kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (89, 1, 2, 3, 4))


if __name__ == "__main__":
    unittest.main()
