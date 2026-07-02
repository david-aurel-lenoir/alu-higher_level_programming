#!/usr/bin/python3
"""Module that defines square_matrix_simple function."""


def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
