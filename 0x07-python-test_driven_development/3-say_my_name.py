#!/usr/bin/python3
"""
Module defines a function for saying a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a message stating a person's name.

    Args:
        - first_name (str): The first name of the person.
        - last_name (str, optional): The last name of the person.
          Defaults to an empty string.

    Raises:
        TypeError: If `first_name` or `last_name` is not a string
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        raise TypeError("{:s} must be a string".format\
                        ("first_name" if isinstance(last_name, str) else "last_name"))
