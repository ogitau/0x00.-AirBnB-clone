#!/usr/bin/python3
"""
create a unique FileStorage instance for your application
"""

from models.engine.file_storage import FileStorage


class HBNBCommand:
    def do_something(self):
        from models import storage
        storage.reload()
