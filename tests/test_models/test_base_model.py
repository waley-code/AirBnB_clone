#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""
import unittest
from models.base_model import BaseModel


class BaseModelTestCase(unittest.TestCase):
    """
    This contains different test cases for the BaseModel class
    """

    def setUp(self):
        """
           set up instances of the BaseModel class
        """
        my_model = BaseModel()


if __name__ == '__main__':
    unittest.main()
