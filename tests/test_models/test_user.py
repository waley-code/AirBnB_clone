#!/usr/bin/python3

from models.user import User
from datetime import datetime
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
        pass

    def test_password(self):
        """Tests password inputs"""
        self.assertEqual(type((self.m).password), str)
        pass

    def test_first_name(self):
        """Tests first_name inputs"""
        self.assertEqual(type((self.m).first_name), str)
        pass

    def test_last_name(self):
        """Tests last_name inputs"""
        self.assertEqual(type((self.m).last_name), str)
        pass


if __name__ == '__main__':
    unittest.main()
