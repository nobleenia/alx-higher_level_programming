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

    Attributes:
        number_of_instances (int): number of instances created and not deleted

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initiatilizes Rectangle with width and height.

        Args:
            width: An integer representing object width.
                  Has a default value of 0.
            height: An integer representing object height.
                  Has a default value of 0
            number_of_instances: An integer representing number of objects.
                  Has a default value of 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """
        Area public attribute

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter public attribute

        Returns:
            The perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance,
        using the character '#'
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rect_pic = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect_pic += str(self.print_symbol)
            rect_pic += "\n"
        return rect_pic[:-1]

    def __repr__(self):
        """
        Return a string representation of the Rectangle instance,
        to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a custom message for del
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
