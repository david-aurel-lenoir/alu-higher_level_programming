#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, using width and height equal to size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
