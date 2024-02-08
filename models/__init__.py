#!/usr/bin/python3
"""
This module initializes a unique instance of FileStorage for the application
"""

# Import the FileStorage class from the file_storage module in the
# models/engine directory
from models.engine.file_storage import FileStorage

# Create the variable storage, an instance of FileStorage
# This will be the unique FileStorage instance
storage = FileStorage()

# Call the reload method on the storage instance
# This will deserialize the JSON file to objects
storage.reload()
