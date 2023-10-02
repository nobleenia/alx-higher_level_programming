#!/usr/bin/python3
"""
Rectangle Class.
This module contains a class that defines a rectangle.
"""


class Rectangle:
    """
    Defines class rectangle with attributes width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """
        Initiatilizes Rectangle with width and height.

        Args:
            width: An integer representing object width.
                  Has a default value of 0.
            height: An integer representing object height.
                  Has a default value of 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width private attribute

        Returns:
            The width private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Validates assignment of the width private attribute

        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height private attribute

        Returns:
            The height private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Validates assignment of the height private attribute.

        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
