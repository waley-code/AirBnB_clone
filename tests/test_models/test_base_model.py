#!/usr/bin/python3

from models.base_model import BaseModel
from datetime import datetime
import unittest
#from unittest.mock import patch

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.m = BaseModel()

    def tearDown(self):
        del self.m
    
    def test_init_attr(self):
        self.assertTrue(self.m.id)
        self.assertIsInstance(self.m.created_at, datetime)
        self.assertIsInstance(self.m.updated_at, datetime)

    def test_str(self):
        eo = f"[{self.m.__class__.__name__}] ({self.m.id}) {self.m.__dict__}"
        
        self.assertEqual(str(self.m), eo)

    def test_to_dict(self):
        dic = self.m.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertIsInstance(dic['updated_at'], str)
        self.assertIsInstance(dic['created_at'], str)

    def test_save(self):
        pre = self.m.updated_at
        self.m.save()
        self.assertNotEqual(self.m.updated_at, pre)

    def test_kwargs(self):
        dic = self.m.to_dict()
        new = BaseModel(**dic)
        new.name = "Joy"
        new.my_number = 7
        new.save()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(new.my_number, 7)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
