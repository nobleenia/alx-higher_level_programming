#!/usr/bin/python3
"""
Square Class
This module contains a class that defines a square
"""


class Square:
    """
    This is a class that defines a square.
    
    Attributes:
    - size (int): The size (side length) of the square.

    Methods:
    - __init__(self, size=0): Initializes a new square with the specified size.
        - size (int): The size of the square (default is 0).
        - Raises:
            - TypeError: If the size is not an integer.
            - ValueError: If the size is less than 0.
    - area(self): Calculate and return the area of the square.
    """
    
    def __init__(self, size=0):
        """
        Initiatilizes Square with size.

        Args:
        - size (int): The size of the square (default is 0).

        Raises:
        TypeError: if not an integer
        ValueError: if less thn 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        - int: The area of the square, which is the square of the side length.
        """
        return self.__size ** 2
