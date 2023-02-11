#!/usr/bin/python3
"""Test suits for State module"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests methods in State class"""

    def setUp(self):
        self.m = State()

    def tearDown(self):
        del self.m

    def test_name(self):
        """Tests name inputs"""
        self.assertEqual(type((self.m).name), str)


if __name__ == '__main__':
    unittest.main()
