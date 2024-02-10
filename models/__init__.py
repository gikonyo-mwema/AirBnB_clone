#!/usr/bin/python3
"""
This module initializes a unique instance of FileStorage for the application
"""

from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
