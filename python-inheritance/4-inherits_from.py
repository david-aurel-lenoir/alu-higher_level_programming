#!/usr/bin/python3
"""Function that checks if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class."""
    return isinstance(obj, a_class) and type(obj) != a_class
