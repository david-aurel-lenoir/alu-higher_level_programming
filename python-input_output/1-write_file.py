#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return the number written.

    Args:
        filename (str): the name of the file to write to.
        text (str): the string to write.

    Returns:
        int: the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
