from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    passhash: str
    mail: str

    class Config:
        orm_mode = True

class Todo(BaseModel):
    id: Optional[int]
    todo_list: Optional[str]
    title: str
    note: Optional[str]
    owner: Optional[User]

    class Config:
        orm_mode = True