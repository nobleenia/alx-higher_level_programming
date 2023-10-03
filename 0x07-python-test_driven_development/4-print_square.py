#!/usr/bin/python3
"""
Module defines a function for printing a square made of '#' characters.
"""


def print_square(size):
    """
    Print a square made of '#' characters.

    Args:
        size (int): The size of the square's sides.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
