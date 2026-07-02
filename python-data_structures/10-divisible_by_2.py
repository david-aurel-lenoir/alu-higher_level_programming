#!/usr/bin/python3
"""Module that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
