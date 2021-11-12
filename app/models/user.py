from . import DB
from pony.orm import db_session, Required, PrimaryKey, Set, commit, select, delete
from typing import Optional, List

class User(DB.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    mail = Required(str, unique=True)
    passhash = Required(str)
    todos = Set("Todo")
    
    @db_session
    def create(username: str, email: str, passhash: str):
        if username == None or passhash == None or email == None:
            raise ValueError("Username, E-Mail or Password can't be None")
        with db_session:
            if User.get(lambda user: user.mail == email):
                raise ValueError("User already exists")
            user = User(name=username, mail=email, passhash=passhash)
            commit()
        return user
    
    @db_session
    def find_by_id(id: int):
        return User[id]

    @db_session
    def find_by_name(name: str) -> List['User']:
        if name is not None:
            user = select(user for user in User if user.mail == name)
            return list(user)
        else:
            return list(user for user in User.select())
    
    @db_session
    def find_users():
        return User.select()
        

    @db_session
    def remove_from_db(user: int):
        User[user].delete()
        return True
    
    @db_session
    def authenticate(username: str, password: str) -> List['User']:
        with db_session:
            user = select(user for user in User if user.mail == username).first()
        if user.passhash == password:
            return user
        return False
    
    @db_session
    def edit_user(id: int, mail: str, name: Optional[str] = None, password: Optional[str] = None):
        user = User[id]
        user.mail = mail or user.mail
        user.name = name or self.name
        user.passhash = password or self.passhash
        commit()