#!/usr/bin/python3
"""Integers division with debug module"""


def safe_print_division(a, b):
    """Divide a by b, print result inside finally, return result or None"""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
