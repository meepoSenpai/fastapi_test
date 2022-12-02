from fastapi import APIRouter, Depends
from typing import List

from ..schemas import schemas
from ..database import DatabaseConnection
from .auth import decode_token

from ..app import DB

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

@router.put("/create", response_model=schemas.Todo)
def create_todo(todo: schemas.Todo, user: DB.user = Depends(decode_token)):
    todo = DB.todo.create(owner=user.id, title=todo.title, note=todo.note or "", todo_list=todo.todo_list or "")
    return todo

@router.get("/", response_model=List[schemas.Todo])
def get_todos(user: DB.user = Depends(decode_token)):
    return list(DB.todo.get_todos_by_user(user.id))

@router.get("/todoLists")
def get_todo_lists(user: DB.user = Depends(decode_token)):
    return list(DB.todo.get_todo_lists(user.id))