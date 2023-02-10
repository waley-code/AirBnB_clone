#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class BaseModelTestCase(unittest.TestCase):
    """
    This contains different test cases for the BaseModel class
    """

    def setUp(self):
        """
           set up instances of the BaseModel class
        """
        self.my_model = BaseModel()

    def tearDown(self):
        """
        destroy instances of the BaseModel class at exit
        """
        del self.my_model

    def test_init_method(self):
        """
        test if the instance of the class has all necessary
        attributes
        """
        self.assertTrue(self.my_model.id)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
