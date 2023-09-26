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
    - my_print(self): Print a representation of the square using '#' characters
    - area(self): Calculate and return the area of the square.
    """
    
    def __init__(self, size=0, position=(0, 0)):
        """
        Initiatilizes Square with size.

        Args:
        - size (int): The size of the square (default is 0).
        - position (tuple): The cordinates of the square position.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Get the position (x, y) of the square.

        Returns:
        - tuple: A tuple containing two positive integers
        representing the position (x, y) of the square.
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """
        Set the position (x, y) of the square to a new value.

        Args:
        - value (tuple): A tuple containing two positive integers representing
        the new position (x, y) to set.

        Raises:
        - TypeError: If value is not a tuple of two positive integers.
        """
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int\
               or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        This method prints a square representation of the object using '#'.
        Each row consists of '#' characters equal to the size of the square.
        If the square has a size of 0, it will print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")
