import jwt
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")
jwt_secret = "somerandomjwtsecret"
router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

def decode_token(token: str = Depends(oauth2_scheme)) -> User:
    decoded_token = dict(jwt.decode(token, jwt_secret, algorithms=['HS256']))
    return User.find_by_id(decoded_token["id"])

@router.post("/")
def authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    if user :=  User.authenticate(username=form_data.username, password=form_data.password):
        token = jwt.encode({"id": user.id, "name": user.name}, jwt_secret)
        return {"access_token": token, "token_type": "bearer"}
    return {"Error": "Username or Password incorrect"}