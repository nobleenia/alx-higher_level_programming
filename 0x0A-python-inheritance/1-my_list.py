#!/usr/bin/python3
"""
Mylist class that extends the built-in `list` class and
provides a method for printing the list in a sorted order
"""


class MyList(list):
    """
    Custom list class that inherits from the built-in `list` class
    """

    def __init__(self):
        """
        Initializes an empty Mylist object.

        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order
        """
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
