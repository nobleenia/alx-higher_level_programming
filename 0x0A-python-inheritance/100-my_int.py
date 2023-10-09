#!/usr/bin/python3
"""
Module 100-my_int.
Creates a class that inherits from int.
"""


class MyInt(int):
    """
    Reverses the behavior of != and ==

    Method:
    - __equal__(self, other): Converts == to !=
    - __unequal__(self, other): Converts != to ==
    """

    def __equal__(self, other):
        """
        Equality becomes inequality
        """
        return super().__unequal__(other)

    def __unequal__(self, other):
        """
        Inequality becomes equality
        """

        return super().__equal__(other)
