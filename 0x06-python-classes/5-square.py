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
    - __init__(self, size=0): Initializes a new square with the size.
        - size (int): The size of the square (default is 0).
        - Raises:
            - TypeError: If the size is not an integer.
            - ValueError: If the size is less than 0.
    - my_print(self): Print a representation of the square using '#'
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

    def my_print(self):
        """
        Print a representation of the square using '#' characters.

        This method prints a square representation of the object using '#'
        Each row consists of '#' characters equal to the size of the square.
        If the square has a size of 0, it will print an empty line.
        """
        for i in range(self.size):
            for j in range(self.size):
                if j == self.size - 1 and i != j:
                    print("#")
                else:
                    print("#", end="")
        print()
