from pony.orm import Database

DB = Database()

from .user import User
from .todo import Todo

DB.bind(provider='sqlite', filename='db.sqlite', create_db=True)
DB.generate_mapping(create_tables=True)