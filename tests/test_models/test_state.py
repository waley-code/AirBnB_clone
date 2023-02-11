#!/usr/bin/python3
"""Test suits for State module"""

import unittest
from datetime import datetime
import models
from models.base_model import BaseModel
from models.state import State


class TestsState(unittest.TestCase):
    """Tests methods in State class"""

    def setUp(self):
        self.m = State()

    def tearDown(self):
        del self.m

    def test_name(self):
        """Tests name inputs"""
        self.assertEqual(type((self.m).name), str)
        pass


if __name__ == '__main__':
    unittest.main()
