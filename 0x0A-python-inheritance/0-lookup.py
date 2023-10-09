#!/usr/bin/python3
"""
Module 0-lookup.
Returns a list of all attributes and methods of an object.
"""


def lookup(obj):
    """
    Return a list of attributes and methods of the object

    Parameters:
    obj (any): The object for which you want to look up attributes and methods.

    Returns:
    list: A list of strings containing the names of attributes and methods
          associated with the input object `obj`
    """
    return dir(obj)
