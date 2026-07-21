#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Inherits from list and adds a sorted-print method."""

    def print_sorted(self):
        """Print the list, sorted in ascending order."""
        print(sorted(self))
