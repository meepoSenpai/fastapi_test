
from fastapi import APIRouter, Depends
from typing import List, Optional

from ..models import schemas
from ..models import user as models
from .auth import decode_token

router = APIRouter(prefix="/user", tags=["User"])

@router.put("/create", response_model=schemas.User, tags=["Data Creation"], summary="Create a new user")
def new_user(user: schemas.User):
    '''
    Creates a user under the condition that the E-Mail is not yet taken.

    - `name`: (Required) Name of the new user.
    - `passhash`: (Required) Password of the user. Will be hashed and salted.
    - `mail`: (Required) E-Mail of the new user. Must be unique in the system. 
    '''
    try:
        user = models.User.create(user.name, user.mail, user.passhash)
        return user
    except ValueError:
        return {"Error" : "User already exists."}

@router.get("/{id}", response_model=schemas.User)
def fetch_by_id(id: int):
    return models.User.find_by_id(id)

@router.get("/search/", response_model=List[schemas.User])
async def fetch_by_name(name: Optional[str] = None):
    users = models.User.find_by_name(name)
    return users

@router.delete("/")
def delete_user(user: models.User = Depends(decode_token)):
    return models.User.remove_from_db(user.id)

@router.patch("/edit")
def edit_user(user: schemas.User, db_user: models.User = Depends(decode_token)):
    models.User.edit_user(id=db_user.id, mail=user.mail, name=user.name, password=user.passhash)

