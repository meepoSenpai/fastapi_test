from . import DB
from pony.orm import db_session, commit, select, delete
from pony.orm import Required, Optional, PrimaryKey

from .user import User

class Todo(DB.Entity):
    id = PrimaryKey(int, auto=True)
    todo_list = Optional(str)
    title = Required(str)
    note = Optional(str)
    owner = Required(User)

    @db_session
    def create(owner: int, title: str, note: str, todo_list: str):
        return Todo(owner=User[owner], title=title, note=note, todo_list=todo_list)
    
    @db_session
    def get_todos_by_user(owner: int):
        return select(todo for todo in Todo if todo.owner == User[owner])[:]

    @db_session
    def get_todo_lists(owner: int):
        return select(todo.todo_list for todo in Todo if todo.owner == User[owner] and todo.todo_list != None or todo.todo_list != "")