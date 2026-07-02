#!/usr/bin/python3
"""Module that defines search_replace function."""


def search_replace(my_list, search, replace):
    return [replace if item == search else item for item in my_list]
