#!/usr/bin/python3
"""Test suits for FileStorage class"""

import unittest
import json
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests methods in FileStorage class"""

    def setUp(self):
        """Sets up instances needed for tests"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.e = f'{self.model.__class__.__name__}.{self.model.id}'

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
        old_f = open('file.json', 'r')
        old_content = old_f.read()
        self.storage.save()
        new_f = open('file.json', 'r')
        new_content = new_f.close()
        self.assertNotEqual(old_content, new_content)
        old_f.close()
        new_f.close()

    def test_reload(self):
        """Tests for the reload method"""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        result = self.storage.all()
        self.assertIn(self.e, result)
