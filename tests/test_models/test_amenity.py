#!/usr/bin/python3
"""Test suits for amenities class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests methods in amenities class"""

    def setUp(self):
        """Instance needed for testing"""
        self.m = Amenity()

    def tearDown(self):
        """removes Instance needed for testing"""
        del self.m

    def test_name(self):
        """Tests name inputs"""
        self.assertEqual(type((self.m).name), str)


if __name__ == '__main__':
    unittest.main()
