#!/usr/bin/python3
"""
Module: BaseGeometry
"""


class BaseGeometry:
    """
    Base class for representing geometric shapes and figures.

    Methods:
    - area(self): calculates the area of the geometry
    - integer_validator(self, name, value): Validates an integer value for a specific attribute.
        - name (str): The name of the attribute being validated.
        - value (int): The value to be validated
    """

    def area(self):
        """
        Raises an exception indicating that it is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Ensure that integer attributes are valid
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    A sub class that inherits from the BaseGeometry

    Methods:
    - __init__(self, width, height): instantiation of class
        - width (int): width of the rectangle
        - height (int): height of the rectangle
    - __str__(self): magic method that returns rectangle description
    - area(self): returns the area of the rectangle
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a formatted string
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        Computes the area of the Rectangle instance
        Overwrites the area() method from BaseGeometry
        """
        return self.__width * self.__height
