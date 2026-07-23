#!/usr/bin/python3
"""Tests unitaires pour la classe Rectangle."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests pour la classe Rectangle."""

    def setUp(self):
        """Réinitialise le compteur __nb_objects avant chaque test."""
        Base._Base__nb_objects = 0

    def test_init_width_height(self):
        """Vérifie l'initialisation de base."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_init_full(self):
        """Vérifie l'initialisation avec tous les paramètres."""
        r = Rectangle(10, 2, 1, 3, 99)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (10, 2, 1, 3, 99))

    def test_width_type_error(self):
        """Vérifie qu'un TypeError est levé pour width non-int."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_width_value_error_zero(self):
        """Vérifie qu'un ValueError est levé si width == 0."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_width_value_error_negative(self):
        """Vérifie qu'un ValueError est levé si width < 0."""
        with self.assertRaises(ValueError):
            Rectangle(-4, 2)

    def test_height_type_error(self):
        """Vérifie qu'un TypeError est levé pour height non-int."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_height_value_error(self):
        """Vérifie qu'un ValueError est levé si height <= 0."""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_x_type_error(self):
        """Vérifie qu'un TypeError est levé pour x non-int."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1")

    def test_x_value_error(self):
        """Vérifie qu'un ValueError est levé si x < 0."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_y_type_error(self):
        """Vérifie qu'un TypeError est levé pour y non-int."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "3")

    def test_y_value_error(self):
        """Vérifie qu'un ValueError est levé si y < 0."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -3)

    def test_area(self):
        """Vérifie le calcul de l'aire."""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_display_basic(self):
        """Vérifie l'affichage simple du rectangle."""
        r = Rectangle(2, 2)
        expected = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_with_position(self):
        """Vérifie l'affichage avec offsets x et y."""
        r = Rectangle(2, 2, 2, 2)
        expected = "\n\n  ##\n  ##\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_str(self):
        """Vérifie la représentation en chaîne."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Vérifie update avec des arguments positionnels."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (89, 1, 2, 3, 4))

    def test_update_args_partial(self):
        """Vérifie update avec des arguments positionnels partiels."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(1, 2)
        self.assertEqual((r.id, r.width), (1, 2))

    def test_update_kwargs(self):
        """Vérifie update avec des kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(width=1, height=2, x=3, y=4, id=89)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (89, 1, 2, 3, 4))

    def test_to_dictionary(self):
        """Vérifie la conversion en dictionnaire."""
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_independent(self):
        """Vérifie que le dictionnaire est indépendant de l'objet original."""
        r = Rectangle(10, 2)
        d = r.to_dictionary()
        d["width"] = 100
        self.assertEqual(r.width, 10)


if __name__ == "__main__":
    unittest.main()
