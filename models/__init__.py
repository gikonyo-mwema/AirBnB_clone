#!/usr/bin/python3
"""
This module initializes a unique instance of FileStorage for the application
"""

from .engine.file_storage import FileStorage


# Create the variable storage, an instance of FileStorage
storage = FileStorage()

# call reload() method on this variable
storage.reload()
