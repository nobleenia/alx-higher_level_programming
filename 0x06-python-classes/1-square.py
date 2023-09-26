#!/usr/bin/python3
"""
Square Class
This module contains a class that defines a square.
"""


class Square:
    """
    This is a class that defines a square.

    Attributes:
    - __size (None): The size of the square defaults to None.

    Methods:
    - __init__(self, size=None): Initializes a new square with the specified size.
        - size (None): The size of the square is not set initially.
    """
    def __init__(self, size=None):
        """
        Initiatilizes Square with size.
        
        Args:
        - size (None): The size of the square is not set initially.
        """
        self.__size = size
