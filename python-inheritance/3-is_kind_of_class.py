#!/usr/bin/python3
"""Defines a function that checks if an object is an instance or subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or a subclass, else False."""
    return isinstance(obj, a_class)
