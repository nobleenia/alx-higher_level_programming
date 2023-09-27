#!/usr/bin/python3
"""
MagicClass
"""
from math import pi


class MagicClass:
    """
    A class that represents a circle and provides methods for calculating
    its area and circumference.

    Attributes:
    - radius (float): The radius of the circle.

    Methods:
    - __init__(self, radius=0): Initializes a new MagicClass
    instance with the
    specified radius.
    - radius (int or float): The radius of the circle (default is 0).
    - Raises:
    - TypeError: If radius is not a number (int or float).
    - area(self): Calculates and returns the area of the circle.
    - Returns:
    - float: The area of the circle.
    - circumference(self): Calculates and returns the circumference
    of the circle.
    - Returns:
    - float: The circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance with the specified radius.

        Args:
        - radius (int or float): The radius of the circle (default is 0).

        Raises:
        - TypeError: If radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
        - float: The area of the circle.
        """
        return self.__radius ** 2 * pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
        - float: The circumference of the circle.
        """
        return 2 * pi * self.__radius
