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
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the size (side length) of the square.
        
        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square to a new value.
        
        Args:
        - value (int): The new size to set.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        - int: The area of the square, which is the square of the side length.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare two Square instances for equality based on their areas.

        Args:
        - other (Square): The other Square instance to compare with.

        Returns:
        - bool: True if the areas are equal, False otherwise.
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """
        Compare two Square instances for inequality based on their areas.

        Args:
        - other (Square): The other Square instance to compare with.

        Returns:
        - bool: True if the areas are not equal, False otherwise.
        """
        return self.__size != other.__size

    def __lt__(self, other):
        """
        Compare two Square instances for less than based on their areas.

        Args:
        - other (Square): The other Square instance to compare with.

        Returns:
        - bool: True if the area of self is less than the area of other, False otherwise.
        """
        return self.__size < other.__size

    def __le__(self, other):
        """
        Compare two Square instances for less than or equal based on their areas.

        Args:
        - other (Square): The other Square instance to compare with.

        Returns:
        - bool: True if the area of self is less than or equal to the area of other, False otherwise.
        """
        return self.__size <= other.__size

    def __gt__(self, other):
        """
        Compare two Square instances for greater than based on their areas.

        Args:
        - other (Square): The other Square instance to compare with.

        Returns:
        - bool: True if the area of self is greater than the area of other, False otherwise.
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """
        Compare two Square instances for greater than or equal based on their areas.

        Args:
        - other (Square): The other Square instance to compare with.

        Returns:
        - bool: True if the area of self is greater than or equal to the area of other, False otherwise.
        """
        return self.__size >= other.__size
