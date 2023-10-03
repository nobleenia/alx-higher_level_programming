#!/usr/bin/python3
"""
LockedClass
Prevents the user from dynamically creating new instance attributes,
except the new instance attribute is called first_name.
"""


class LockedClass:
    """
    Restricts the creation of new instance attributes,
    allowing only the 'first_name' attribute to be assigned dynamically.
    """
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """
        Initializes a LockedClass instance

        Args:
            first_name (str, optional): The value to assign to the 'first_name'
            Defaults to an empty string.
        """
        self.first_name = first_name
