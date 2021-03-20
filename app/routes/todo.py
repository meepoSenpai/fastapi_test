from fastapi import APIRouter, Depends
from typing import List

from ..models import schemas
from ..models import todo as models
from ..models.user import User
from .auth import decode_token

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

@router.put("/create", response_model=schemas.Todo)
def create_todo(todo: schemas.Todo, user: User = Depends(decode_token)):
    todo = models.Todo.create(owner=user.id, title=todo.title, note=todo.note or "", todo_list=todo.todo_list or "")
    return todo

@router.get("/", response_model=List[schemas.Todo])
def get_todos(user: User = Depends(decode_token)):
    return list(models.Todo.get_todos_by_user(user.id))

@router.get("/todoLists")
def get_todo_lists(user: User = Depends(decode_token)):
    return list(models.Todo.get_todo_lists(user.id))