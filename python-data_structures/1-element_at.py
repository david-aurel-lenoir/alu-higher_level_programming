#!/usr/bin/python3
"""A  function that retrieves an element from a list like in C."""


def element_at(my_list, idx):
    """Return the element of my_list at index idx, or None if out of range."""
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
