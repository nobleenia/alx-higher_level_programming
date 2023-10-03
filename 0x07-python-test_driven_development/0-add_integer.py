#!/usr/bin/python3
"""
Module contains a function for adding two integers or floats
`add_integer(a, b=98)`, takes two numeric arguments `a` and `b`
(with a default value of 98) and returns their sum as an integer.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int or float): The first numeric value to be added.
        b (int or float, optional): The second numeric value to be added.
        Defaults to 98 if not provided.

    Returns:
        int: The integer result of adding `a` and `b`.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
