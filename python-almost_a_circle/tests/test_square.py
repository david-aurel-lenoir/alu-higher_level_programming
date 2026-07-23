#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def setUp(self):
        """Reset the __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_is_rectangle_subclass(self):
        """Check that Square inherits from Rectangle."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)

    def test_square_one_arg(self):
        """Check Square(1) instantiation with only size."""
        s = Square(1)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 0, 0))

    def test_square_two_args(self):
        """Check Square(1, 2) instantiation with size and x."""
        s = Square(1, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 0))

    def test_square_three_args(self):
        """Check Square(1, 2, 3) instantiation with size, x, y."""
        s = Square(1, 2, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 3))

    def test_square_four_args(self):
        """Check Square(1, 2, 3, 4) instantiation with id."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(
            (s.width, s.height, s.x, s.y, s.id), (1, 1, 2, 3, 4)
        )

    def test_size_string_type_error(self):
        """Check TypeError is raised when size is a string."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_string_type_error(self):
        """Check TypeError is raised when x is a string."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_string_type_error(self):
        """Check TypeError is raised when y is a string."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_id_string_no_error(self):
        """Check id accepts any type since it is not validated."""
        s = Square(1, 2, 3, "4")
        self.assertEqual(s.id, "4")

    def test_size_negative_value_error(self):
        """Check ValueError is raised when size < 0."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_negative_value_error(self):
        """Check ValueError is raised when x < 0."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative_value_error(self):
        """Check ValueError is raised when y < 0."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_size_zero_value_error(self):
        """Check ValueError is raised when size == 0."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Check the string representation."""
        s = Square(5, 1, 2, 12)
        self.assertEqual(str(s), "[Square] (12) 1/2 - 5")

    def test_to_dictionary(self):
        """Check to_dictionary() exists and returns correct values."""
        s = Square(10, 2, 1, 5)
        expected = {"id": 5, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_to_dictionary_independent(self):
        """Check the returned dict is independent of the instance."""
        s = Square(10)
        d = s.to_dictionary()
        d["size"] = 100
        self.assertEqual(s.size, 10)

    def test_size_getter(self):
        """Check that size returns the width value."""
        s = Square(7)
        self.assertEqual(s.size, 7)

    def test_size_setter(self):
        """Check that the size setter updates both width and height."""
        s = Square(7)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_area(self):
        """Check the area calculation for a square."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_update_no_args(self):
        """Check update() with no arguments does nothing."""
        s = Square(10, 10, 10, 1)
        s.update()
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 10, 10, 10))

    def test_update_one_arg(self):
        """Check update(89) updates only id."""
        s = Square(10, 10, 10, 1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_two_args(self):
        """Check update(89, 1) updates id and size."""
        s = Square(10, 10, 10, 1)
        s.update(89, 1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_three_args(self):
        """Check update(89, 1, 2) updates id, size, x."""
        s = Square(10, 10, 10, 1)
        s.update(89, 1, 2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_four_args(self):
        """Check update(89, 1, 2, 3) updates id, size, x, y."""
        s = Square(10, 10, 10, 1)
        s.update(89, 1, 2, 3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_update_kwargs_id(self):
        """Check update(**{'id': 89}) updates only id."""
        s = Square(10, 10, 10, 1)
        s.update(**{"id": 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_size(self):
        """Check update with id and size kwargs."""
        s = Square(10, 10, 10, 1)
        s.update(**{"id": 89, "size": 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_kwargs_x(self):
        """Check update with id, size and x kwargs."""
        s = Square(10, 10, 10, 1)
        s.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_kwargs_full(self):
        """Check update with all attributes as kwargs."""
        s = Square(10, 10, 10, 1)
        s.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_create_kwargs_id(self):
        """Check Square.create with only id."""
        s = Square.create(**{"id": 89})
        self.assertEqual(s.id, 89)

    def test_create_kwargs_size(self):
        """Check Square.create with id and size."""
        s = Square.create(**{"id": 89, "size": 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_kwargs_x(self):
        """Check Square.create with id, size and x."""
        s = Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_create_kwargs_full(self):
        """Check Square.create with all attributes."""
        d = {"id": 89, "size": 1, "x": 2, "y": 3}
        s = Square.create(**d)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_save_to_file_none(self):
        """Check Square.save_to_file(None) creates a valid file."""
        import os
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_save_to_file_empty(self):
        """Check Square.save_to_file([]) creates a valid file."""
        import os
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_list(self):
        """Check Square.save_to_file([Square(1)])."""
        import os
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_load_from_file_no_file(self):
        """Check Square.load_from_file() when file doesn't exist."""
        import os
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Check Square.load_from_file() when file exists."""
        import os
        Square.save_to_file([Square(5, 1, 2, 89)])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
