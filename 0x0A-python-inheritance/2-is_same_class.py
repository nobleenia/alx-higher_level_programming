#!/usr/bin/python3
"""
Module: is_same_class

Usage:
    - is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    Checks if an object belongs to a specific class or is an instance of that class

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object belongs to the specified class, False otherwise.

    """
    if type(obj) is a_class:
        return True
    else:
        return False
