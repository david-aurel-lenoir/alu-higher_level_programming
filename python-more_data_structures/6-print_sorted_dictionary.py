#!/usr/bin/python3
"""Module that defines print_sorted_dictionary function."""


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
