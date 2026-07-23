#!/usr/bin/python3
"""Tests unitaires pour la classe Square."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests pour la classe Square."""

    def setUp(self):
        """Réinitialise le compteur __nb_objects avant chaque test."""
        Base._Base__nb_objects = 0

    def test_is_rectangle_subclass(self):
        """Vérifie que Square hérite de Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_init_size_only(self):
        """Vérifie l'initialisation avec seulement la taille."""
        s = Square(5)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 0, 0))
        self.assertEqual(s.id, 1)

    def test_init_full(self):
        """Vérifie l'initialisation complète."""
        s = Square(5, 1, 2, 99)
        self.assertEqual((s.width, s.height, s.x, s.y, s.id),
                         (5, 5, 1, 2, 99))

    def test_size_type_error(self):
        """Vérifie qu'un TypeError est levé pour size non-int."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_value_error(self):
        """Vérifie qu'un ValueError est levé si size <= 0."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_getter(self):
        """Vérifie que size retourne bien la largeur."""
        s = Square(7)
        self.assertEqual(s.size, 7)

    def test_size_setter(self):
        """Vérifie que le setter size modifie width et height."""
        s = Square(7)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_area(self):
        """Vérifie le calcul de l'aire d'un carré."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Vérifie la représentation en chaîne."""
        s = Square(5, 1, 2, 12)
        self.assertEqual(str(s), "[Square] (12) 1/2 - 5")

    def test_update_args(self):
        """Vérifie update avec des arguments positionnels."""
        s = Square(10, 10, 10, 1)
        s.update(89, 1, 2, 3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_update_kwargs(self):
        """Vérifie update avec des kwargs."""
        s = Square(10, 10, 10, 1)
        s.update(size=1, x=2, y=3, id=89)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_to_dictionary(self):
        """Vérifie la conversion en dictionnaire."""
        s = Square(10, 2, 1, 5)
        expected = {"id": 5, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_to_dictionary_independent(self):
        """Vérifie que le dictionnaire est indépendant de l'objet original."""
        s = Square(10)
        d = s.to_dictionary()
        d["size"] = 100
        self.assertEqual(s.size, 10)


if __name__ == "__main__":
    unittest.main()
