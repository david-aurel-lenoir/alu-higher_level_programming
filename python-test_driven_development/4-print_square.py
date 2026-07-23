#!/usr/bin/python3
"""Module that defines a function to print a square of a given size.

This module provides the print_square function, which prints a
square made of the '#' character with the given side length.
"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): the size length of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
