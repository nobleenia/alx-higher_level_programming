#!/usr/bin/python3
"""
Unittest for max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestCase for the max_integer function
    """

    def test_regular(self):
        """
        Test with regular list of integer
        (should return the max result)
        """
        list1 = [7, 6, 1, 2, 5]
        result = max_integer(list1)
        self.assertEqual(result, 7)

    def test_not_int(self):
        """
        Test with list of non-integer and integer
        (should raise a TypeError exception)
        """
        list1 = ["hello", "world", 3]
        self.assertRaises(TypeError, max_integer, list1)

    def test_empty(self):
        """
        Test with an empty list
        (should return None)
        """
        list1 = []
        result = max_integer(list1)
        self.assertEqual(result, None)

    def test_negative(self):
        """
        Test with list of negative values
        (should return maximum value)
        """
        list1 = [-7, -9, -3]
        result = max_integer(list1)
        self.assertEqual(result, -3)

    def test_float(self):
        """
        Test with a list of mixed integers and floats
        (should return maximum value)
        """
        list1 = [4, 4.5, 6.2]
        result = max_integer(list1)
        self.assertEqual(result, 6.2)

    def test_not_list(self):
        """
        Test with a parameter not a list
        (should raise a TypeError)
        """
        self.assertRaises(TypeError, max_integer, 3)

    def test_unique(self):
        """
        Test with a list having just one integer
        (should return the value of integer in list1)
        """
        list1 = [53]
        result = max_integer(list1)
        self.assertEqual(result, 53)

    def test_identical(self):
        """
        Test with a list of identical values: 
        (should return one of the equal value)
        """
        list1 = [6, 6, 6, 6]
        result = max_integer(list1)
        self.assertEqual(result, 6)

    def test_strings(self):
        """
        Test with a list of strings
        (should return the first string)
        """
        list1 = ["hello", "world"]
        result = max_integer(list1)
        self.assertEqual(result, "hello")

    def test_none(self):
        """
        Test with  'None' as parameter
        (should raise a TypeError)
        """
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
