#!/usr/bin/python3
"""Test suits for city module"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests methods in City class"""

    def setUp(self):
        """Instance needed for testing"""
        self.m = City()

    def tearDown(self):
        """removes Instance needed for testing"""
        del self.m

    def test_state_id(self):
        """Tests state_id inputs"""
        self.assertEqual(type((self.m).state_id), str)

    def test_name(self):
        """Tests name inputs"""
        self.assertEqual(type((self.m).name), str)


if __name__ == '__main__':
    unittest.main()
