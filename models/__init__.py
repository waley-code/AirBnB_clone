#!/usr/bin/python3
"""
links BaseModel to FileStorage by using the variable storage
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
