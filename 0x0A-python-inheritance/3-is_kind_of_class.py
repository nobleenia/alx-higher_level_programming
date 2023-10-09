#!/usr/bin/python3
"""
Module: is_kind_of_class
"""



def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or a subclass of that class

    Args:
    - obj (object): The object to be checked.
    - a_class (type): The class or type to compare with.

    Returns:
    - bool: True if the object is an instance of the specified
    class or its subclass; otherwise, False
    """
    return isinstance(obj, a_class)
