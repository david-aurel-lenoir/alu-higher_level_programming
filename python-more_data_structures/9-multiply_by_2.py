#!/usr/bin/python3
"""Module that defines a function to multiply dictionary values by 2."""


def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
