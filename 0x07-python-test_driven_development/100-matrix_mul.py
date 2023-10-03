#!/usr/bin/python3
"""
matrix_mul
Module defines a function for matrix multiplication
"""
def matrix_mul(m_a, m_b):
    """
    Perform matrix multiplication on two matrices and return the result.

    Args:
        - m_a (list of lists): The first matrix to be multiplied.
        - m_b (list of lists): The second matrix to be multiplied.

    Returns:
        list of lists: The result of matrix multiplication.

    Raises:
        ValueError: If either `m_a` or `m_b` is empty or contains empty lists,
        or if the matrices cannot be multiplied due to incompatible dimensions.
        TypeError: If `m_a` or `m_b` is not a list of lists,
        or if the elements of the matrices are not integers or floats.
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in matrix_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in matrix_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(matrix_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inv_b = []
    for i in range(len(m_b[0])):
        new_row = []
        for j in range(len(m_b)):
            new_row.append(m_b[j][i])
        inv_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inv_b:
            product = 0
            for i in range(len(inv_b[0])):
                product += row[i] * col[i]
            new_row.append(product)
        new_matrix.append(new_row)

    return new_matrix
