#!/usr/bin/python3
"""Test suits for Review module"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests methods in State class"""

    def setUp(self):
        self.m = Review()

    def tearDown(self):
        del self.m

    def test_place_id(self):
        """Tests name inputs"""
        self.assertEqual(type((self.m).place_id), str)

    def test_user_id(self):
        """Tests name inputs"""
        self.assertEqual(type((self.m).user_id), str)

    def test_text(self):
        """Tests name inputs"""
        self.assertEqual(type((self.m).text), str)


if __name__ == '__main__':
    unittest.main()
