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
