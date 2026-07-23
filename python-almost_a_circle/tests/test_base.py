#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Reset the __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_public(self):
        """Check that id is a public attribute."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        """Check that id auto-increments when None is passed."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_none_after_manual(self):
        """Check the counter keeps incrementing after a manual id."""
        b1 = Base(89)
        b2 = Base()
        self.assertEqual(b1.id, 89)
        self.assertEqual(b2.id, 1)

    def test_to_json_string_none(self):
        """Check that None returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Check that an empty list returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Check JSON conversion of a list of dictionaries."""
        list_dicts = [{"id": 12}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(type(result), str)

    def test_to_json_string_return_type(self):
        """Check that to_json_string returns a string."""
        list_dicts = [{"id": 12}]
        self.assertIsInstance(Base.to_json_string(list_dicts), str)

    def test_from_json_string_none(self):
        """Check that None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Check that '[]' returns an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        """Check conversion of a valid JSON string into a list."""
        json_str = '[{ "id": 89 }]'
        self.assertEqual(Base.from_json_string(json_str), [{"id": 89}])

    def test_from_json_string_return_type(self):
        """Check that from_json_string returns a list."""
        json_str = '[{ "id": 89 }]'
        self.assertIsInstance(Base.from_json_string(json_str), list)

    def test_save_to_file_none(self):
        """Check that save_to_file(None) creates a file containing '[]'."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_list(self):
        """Check saving a list of rectangles to a JSON file."""
        r1 = Rectangle(1, 2)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn("width", content)
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Check that load_from_file returns [] when no file exists."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_when_file_exists(self):
        """Check that save then load preserves rectangle data."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        list_rects = Rectangle.load_from_file()
        self.assertEqual(len(list_rects), 2)
        self.assertEqual(str(list_rects[0]), str(r1))
        self.assertEqual(str(list_rects[1]), str(r2))
        os.remove("Rectangle.json")

    def test_save_to_file_csv_rectangle(self):
        """Check saving rectangles to a CSV file."""
        r1 = Rectangle(1, 2)
        Rectangle.save_to_file_csv([r1])
        self.assertTrue(os.path.exists("Rectangle.csv"))
        os.remove("Rectangle.csv")

    def test_load_from_file_csv_rectangle(self):
        """Check saving then loading rectangles in CSV format."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r1])
        list_rects = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rects), 1)
        self.assertEqual(str(list_rects[0]), str(r1))
        os.remove("Rectangle.csv")

    def test_save_load_from_file_csv_square(self):
        """Check saving and loading squares in CSV format."""
        s1 = Square(5, 1, 2, 1)
        Square.save_to_file_csv([s1])
        list_sq = Square.load_from_file_csv()
        self.assertEqual(len(list_sq), 1)
        self.assertEqual(str(list_sq[0]), str(s1))
        os.remove("Square.csv")

    def test_create_rectangle_id(self):
        """Check the create method for Rectangle with only id."""
        r1 = Rectangle.create(**{"id": 89})
        self.assertEqual(r1.id, 89)

    def test_create_rectangle_width(self):
        """Check the create method for Rectangle with id and width."""
        r1 = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual((r1.id, r1.width), (89, 1))

    def test_create_rectangle_full(self):
        """Check the create method for Rectangle with all attributes."""
        d = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        r1 = Rectangle.create(**d)
        self.assertEqual(
            (r1.id, r1.width, r1.height, r1.x, r1.y), (89, 1, 2, 3, 4)
        )

    def test_create_rectangle_independent(self):
        """Check that create returns a distinct instance."""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square_id(self):
        """Check the create method for Square with only id."""
        s1 = Square.create(**{"id": 89})
        self.assertEqual(s1.id, 89)

    def test_create_square_size(self):
        """Check the create method for Square with id and size."""
        s1 = Square.create(**{"id": 89, "size": 1})
        self.assertEqual((s1.id, s1.size), (89, 1))

    def test_create_square_full(self):
        """Check the create method for Square with all attributes."""
        d = {"id": 89, "size": 1, "x": 2, "y": 3}
        s1 = Square.create(**d)
        self.assertEqual((s1.id, s1.size, s1.x, s1.y), (89, 1, 2, 3))

    def test_create_square_independent(self):
        """Check that create returns a distinct instance."""
        s1 = Square(3, 1, 2)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_rectangle_save_to_file_none(self):
        """Check Rectangle.save_to_file(None) creates a valid file."""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

    def test_rectangle_save_to_file_list(self):
        """Check Rectangle.save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

    def test_rectangle_load_from_file_no_file(self):
        """Check Rectangle.load_from_file() when file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangle_load_from_file_exists(self):
        """Check Rectangle.load_from_file() when file exists."""
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)
        os.remove("Rectangle.json")

    def test_square_save_to_file_none(self):
        """Check Square.save_to_file(None) creates a valid file."""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_square_save_to_file_empty(self):
        """Check Square.save_to_file([]) creates a valid file."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_square_save_to_file_list(self):
        """Check Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_square_load_from_file_no_file(self):
        """Check Square.load_from_file() when file doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_square_load_from_file_exists(self):
        """Check Square.load_from_file() when file exists."""
        Square.save_to_file([Square(5, 1, 2, 89)])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
