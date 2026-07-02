#!/usr/bin/python3
"""Module that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    biggest = my_list[0]
    for number in my_list:
        if number > biggest:
            biggest = number

    return biggest
