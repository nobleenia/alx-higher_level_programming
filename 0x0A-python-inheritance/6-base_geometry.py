#!/usr/bin/python3
"""
Module: BaseGeometry
"""


class BaseGeometry:
    """
    Base class for representing geometric shapes and figures.

    Methods:
    - area(self): calculates the area of the geometry
    """

    def area(self):
        """
        Raises an exception indicating that it is not implemented
        """
        raise Exception("area() is not implemented")
