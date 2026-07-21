#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): the name of the JSON file to read.

    Returns:
        the Python data structure represented by the file's content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
