#!/usr/bin/python3
"""Module that defines a function to print a person's full name.

This module provides the say_my_name function, which takes a first
name and an optional last name, and prints
"My name is <first name> <last name>".
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>.

    Args:
        first_name (str): the first name.
        last_name (str): the last name, defaults to an empty string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
