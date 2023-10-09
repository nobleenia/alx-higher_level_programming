#!/usr/bin/python3
"""
Module: inherits_from
"""



def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class inherited
    (directly or indirectly) from the specified class

    Args:
    - obj (object): The object to be checked.
    - a_class (type): The class or type to compare with.

    Returns:
    - bool: True if the object is an instance of the specified
    class or its subclass; otherwise, False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
