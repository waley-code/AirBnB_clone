#!/usr/bin/python3
"""This module contains unittests for User class"""

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Tests methods in User class"""

    def setUp(self):
        self.m = User()

    def tearDown(self):
        del self.m

    def test_Email(self):
        """Tests state_id inputs"""
        self.assertEqual(type((self.m).email), str)

    def test_password(self):
        """Tests password inputs"""
        self.assertEqual(type((self.m).password), str)

    def test_first_name(self):
        """Tests first_name inputs"""
        self.assertEqual(type((self.m).first_name), str)

    def test_last_name(self):
        """Tests last_name inputs"""
        self.assertEqual(type((self.m).last_name), str)


if __name__ == '__main__':
    unittest.main()
