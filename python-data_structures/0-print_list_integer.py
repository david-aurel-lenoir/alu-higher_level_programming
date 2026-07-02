#!/usr/bin/python3
"""Module that prints all integers of a list"""


def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line."""
    for number in my_list:
        print("{:d}".format(number))
