#!/usr/bin/python3
"""Init.py"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
