#!/usr/bin/python3
"""Safe printing of an integer module"""


def safe_print_integer(value):
    """Print value as an integer, return True if successful, else False"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
