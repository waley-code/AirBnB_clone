#!/usr/bin/python3
"""Test suits for FileStorage class"""

import unittest
import json
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import path


class TestFileStorage(unittest.TestCase):
    """Tests methods in FileStorage class"""

    def setUp(self):
        """Sets up instances needed for tests"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model_2 = BaseModel()
        self.file_path = "file.json"
        self.e = f'{self.model.__class__.__name__}.{self.model.id}'
        self.f = f'{self.model_2.__class__.__name__}.{self.model_2.id}'

    def test_all(self):
        """Tests for the all method"""
        self.storage.new(self.model)
        result = self.storage.all()
        self.assertIsInstance(result, dict)
        self.assertIn(self.e, result)

    def test_new(self):
        """Tests for the new method"""
        self.storage.new(self.model)
        result = self.storage.all()
        self.assertIn(self.e, result)

    def test_save(self):
        """Tests for the save method"""
        self.storage.new(self.model)
        self.storage.new(self.model_2)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        self.assertIn(self.e, data.keys())
        self.assertIn(self.f, data.keys())

    def test_reload(self):
        """Tests for the reload method"""
        self.storage.new(self.model)
        self.storage.save()
        file_storage_2 = FileStorage()
        file_storage_2.reload()
        result = file_storage_2.all().keys()
        self.assertIn(self.e, result)
