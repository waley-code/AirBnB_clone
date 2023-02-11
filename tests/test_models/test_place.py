#!/usr/bin/python3
"""Test suits for place module"""
import unittest
from datetime import datetime
import models
from models.base_model import BaseModel
from models.place import Place


class TestsPlace(unittest.TestCase):
    """Tests methods in place class"""

    def setUp(self):
        """Instance needed for testing"""
        self.m = Place()

    def tearDown(self):
        """removes Instance needed for testing"""
        del self.m

    def test_city_id(self):
        """Tests city_id inputs"""
        self.assertEqual(type((self.m).city_id), str)
        pass

    def test_user_id(self):
        """Tests user_id inputs"""
        self.assertEqual(type((self.m).user_id), str)
        pass

    def test_name(self):
        """Tests name inputs"""
        self.assertEqual(type((self.m).name), str)
        pass

    def test_description(self):
        """Tests description inputs"""
        self.assertEqual(type((self.m).description), str)
        pass

    def test_number_rooms(self):
        """Tests number_rooms inputs"""
        self.assertEqual(type((self.m).number_rooms), int)
        pass

    def test_number_bathrooms(self):
        """Tests number_bathrooms inputs"""
        self.assertEqual(type((self.m).number_bathrooms), int)
        pass

    def test_max_guest(self):
        """Tests number_bathrooms inputs"""
        self.assertEqual(type((self.m).max_guest), int)
        pass

    def test_price_by_night(self):
        """Tests price_by_night inputs"""
        self.assertEqual(type((self.m).price_by_night), int)
        pass

    def test_latitude(self):
        """Tests latitude inputs"""
        self.assertEqual(type((self.m).latitude), float)
        pass

    def test_longitude(self):
        """Tests longitude inputs"""
        self.assertEqual(type((self.m).longitude), float)
        pass

    def test_amenity_ids(self):
        """Tests amenity_ids inputs"""
        self.assertEqual(type((self.m).amenity_ids), list)
        pass


if __name__ == '__main__':
    unittest.main()
