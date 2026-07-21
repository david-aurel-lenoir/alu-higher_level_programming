#!/usr/bin/python3
"""Defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a UTF8 text file and return the number written.

    Args:
        filename (str): the name of the file to append to.
        text (str): the string to append.

    Returns:
        int: the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
