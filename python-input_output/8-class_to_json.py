#!/usr/bin/python3
"""Defines a function that returns the dict representation of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: an instance of a class with serializable attributes.

    Returns:
        dict: the object's instance attributes.
    """
    return obj.__dict__
