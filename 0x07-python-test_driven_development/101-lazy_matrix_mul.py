#!/usr/bin/python3
"""
lazy_matrix_mul
Module defines a function for performing matrix multiplication using NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Perform matrix multiplication on two matrices using NumPy and return the result.

    Args:
        m_a (numpy.ndarray): The first matrix to be multiplied.
        m_b (numpy.ndarray): The second matrix to be multiplied.

    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """
    return numpy.matmul(m_a, m_b)
