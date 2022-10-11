#!/usr/bin/python3
"""This module instantiates an object of FileStorage or DBStorage"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.files_storage import FileStorage
    storage = FileStorage()
    storage.reload()