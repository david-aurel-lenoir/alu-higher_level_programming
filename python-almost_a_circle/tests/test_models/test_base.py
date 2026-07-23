#!/usr/bin/python3
"""Tests unitaires pour la classe Base."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests pour la classe Base."""

    def setUp(self):
        """Réinitialise le compteur __nb_objects avant chaque test."""
        Base._Base__nb_objects = 0

    def test_id_public(self):
        """Vérifie que l'id est bien un attribut public."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        """Vérifie que l'id s'incrémente automatiquement si None."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_none_after_manual(self):
        """Vérifie que le compteur continue même après un id manuel."""
        b1 = Base(50)
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_to_json_string_empty(self):
        """Vérifie qu'une liste vide retourne '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Vérifie qu'une liste None retourne '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_list(self):
        """Vérifie la conversion JSON d'une liste de dictionnaires."""
        list_dicts = [{"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(type(result), str)

    def test_from_json_string_empty(self):
        """Vérifie qu'une chaîne vide/None retourne une liste vide."""
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_valid(self):
        """Vérifie la conversion d'une chaîne JSON valide en liste."""
        json_str = '[{"id": 1, "width": 10, "height": 2, "x": 0, "y": 0}]'
        result = Base.from_json_string(json_str)
        self.assertEqual(result, [
            {"id": 1, "width": 10, "height": 2, "x": 0, "y": 0}
        ])

    def test_save_to_file_none(self):
        """Vérifie que save_to_file([]) crée un fichier avec '[]'."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_list(self):
        """Vérifie la sauvegarde d'une liste de rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn("width", content)
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Vérifie que load_from_file retourne [] si le fichier n'existe pas."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_load_from_file(self):
        """Vérifie que save_to_file suivi de load_from_file préserve les données."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        list_rects = Rectangle.load_from_file()
        self.assertEqual(len(list_rects), 2)
        self.assertEqual(str(list_rects[0]), str(r1))
        self.assertEqual(str(list_rects[1]), str(r2))
        os.remove("Rectangle.json")

    def test_save_load_from_file_csv(self):
        """Vérifie la sauvegarde et le chargement CSV."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rects = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rects), 2)
        self.assertEqual(str(list_rects[0]), str(r1))
        os.remove("Rectangle.csv")

    def test_save_load_from_file_csv_square(self):
        """Vérifie la sauvegarde et le chargement CSV pour Square."""
        s1 = Square(5, 1, 2, 1)
        Square.save_to_file_csv([s1])
        list_sq = Square.load_from_file_csv()
        self.assertEqual(len(list_sq), 1)
        self.assertEqual(str(list_sq[0]), str(s1))
        os.remove("Square.csv")

    def test_create_rectangle(self):
        """Vérifie la méthode create pour Rectangle."""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Vérifie la méthode create pour Square."""
        s1 = Square(3, 1, 2)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


if __name__ == "__main__":
    unittest.main()
