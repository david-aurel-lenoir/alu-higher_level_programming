#!/usr/bin/python3
"""Module that defines a function to divide all elements of a matrix.

This module provides the matrix_divided function, which takes a
matrix (list of lists of ints/floats) and a divisor, and returns a
new matrix with every element divided by the divisor, rounded to 2
decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix (list): a list of lists of integers or floats.
        div (int/float): the divisor.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if row == [] or not all(
                isinstance(n, (int, float)) and not isinstance(n, bool)
                for n in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(n / div, 2) for n in row] for row in matrix]
