#!/usr/bin/python3
"""
This module contains the TestBaseModel class
"""
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """all unit test cases for the BaseModel class
    """
    def setUp(self):
        """create instances of the BaseModel class
        """
        self.bm = BaseModel()

    def tearDown(self):
        """deletes all instances created at exit
        """
        del self.bm

    def test_init(self):
        """unit test for the __init__ method
        """
        self.assertTrue(self.bm.id)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

        dic = self.bm.to_dict()
        new = BaseModel(**dic)
        new.name = "Joy"
        new.my_number = 7
        new.save()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(new.my_number, 7)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)

    def test_str(self):
        """ unit test for the string representation"""
        eo = f"[{self.bm.__class__.__name__}] ({self.bm.id})"
        eo_c = f" {self.bm.__dict__}"

        self.assertEqual(str(self.bm), eo + eo_c)

    def test_to_dict(self):
        """test the dictionary method"""
        dic = self.bm.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertIsInstance(dic['updated_at'], str)
        self.assertIsInstance(dic['created_at'], str)

    def test_save(self):
        """ test the save method"""
        pre = self.bm.updated_at
        self.bm.save()

    def test_instantiation(self):
        """tests all instantiation of BaseModel"""
        self.assertIsInstance(self.bm, BaseModel)
        self.assertIsNotNone(self.bm.id)

    def test_instance_updated_at(self):
        """tests all instance of updated_at of BaseModel"""
        self.assertIsNotNone(self.bm.updated_at)

    def test_instance_created_at(self):
        """tests all instance created_at of BaseModel"""
        self.assertIsNotNone(self.bm.created_at)

    def test_to_dict_classObj(self):
        """Tests for class in dictionary convertion"""
        dic_obj = self.bm.to_dict()
        self.assertIn('__class__', dic_obj)
        self.assertEqual(dic_obj['__class__'], 'BaseModel')

    def test_to_dict_createdAt(self):
        """Tests for created_at in dictionary convertions"""
        dic_obj = self.bm.to_dict()
        self.assertIn('created_at', dic_obj)
        self.assertIsInstance(dic_obj['created_at'], str)

    def test_to_dict_updated_at(self):
        """Tests for updated_at in dictionary convertions"""
        dic_obj = self.bm.to_dict()
        self.assertIn('updated_at', dic_obj)
        self.assertIsInstance(dic_obj['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
