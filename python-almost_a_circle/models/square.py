#!/usr/bin/python3
"""Module that defines the Square class, inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): Size of the square's side.
            x (int): X position of the square.
            y (int): Y position of the square.
            id (int): Identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (updates width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Update attributes via positional or keyword arguments.

        Args order (if using *args): id, size, x, y.
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
