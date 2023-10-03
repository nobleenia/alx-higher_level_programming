#!/usr/bin/python3
"""
Module contains a function that
divides all elements of a matrix by a divisor
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        - matrix (list of lists): The input matrix containing
        integers or floats.
        - div (int or float): The divisor which divides matrix elements

    Returns:
        list of lists: A new matrix results to two decimal places

    Raises:
        TypeError: If 'div' is not a number, 'matrix' is not a valid matrix,
                   if 'matrix' contains non-numeric values,
                   if rows of the matrix have different sizes.
        ZeroDivisionError: If 'div' is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError\
            ("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []
    matrix_len = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError\
                ("matrix must be a matrix (list of lists) of integers/floats")
        if len(lists) != matrix_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError\
                    ("matrix must be a matrix (list of lists) of integers/floats")
            new_list.append(round(i/div, 2))
        new_matrix.append(new_list)
    return new_matrix
