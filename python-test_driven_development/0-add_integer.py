#!/usr/bin/python3
"""Module that defines a function to add two integers.

This module provides the add_integer function, which takes two
numbers (integers or floats), casts them to integers if needed,
and returns their sum.
"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int/float): the first number.
        b (int/float): the second number, defaults to 98.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
