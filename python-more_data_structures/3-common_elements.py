#!/usr/bin/python3
"""Module that defines common_elements function."""


def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets.

    Args:
        set_1 (set): the first set.
        set_2 (set): the second set.

    Returns:
        A new set containing the common elements between set_1 and set_2.
    """
    return set_1 & set_2
