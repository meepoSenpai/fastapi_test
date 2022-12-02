from pydantic import BaseModel

class User(BaseModel):
    name: str
    passhash: str
    mail: str

    class Config:
        orm_mode = True

class Todo(BaseModel):
    id: int | None = None
    todo_list: str | None = None
    title: str
    note: str | None = None
    owner: User | None = None

    class Config:
        orm_mode = True