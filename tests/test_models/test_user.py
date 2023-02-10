#!/usr/bin/python3

from models.user import User
from datetime import datetime
import unittest
#from unittest.mock import patch

class TestUser(unittest.TestCase):

    def setUp(self):
        self.m = User()

    def tearDown(self):
        del self.m
        
    

if __name__ == '__main__':
    unittest.main()
