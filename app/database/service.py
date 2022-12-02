from pony.orm import Database, db_session, select

DB = Database()

from .user import User
from .todo import Todo

class DatabaseConnection:

    state = {"is_initialized": False, "db": DB}

    def __init__(self, filename: str = None):
        filename = f"/tmp/{filename}"
        self.__dict__ = DatabaseConnection.state
        if not self.is_initialized and filename:
            DB.bind(provider='sqlite', filename=filename)
            DB.generate_mapping(create_tables=True)
            self.user = User
            self.todo = Todo
            self.is_initialized = True
    
    @db_session
    def create_user(self, name: str, passhash: str, email: str):
        if select (user for user in self.user if user.mail == email):
            raise ValueError()
        self.user(name, passhash, email)