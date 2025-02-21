from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from starlette import status
from models import Users
from passlib.context import CryptContext
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SECRET_KEY = "bf21c4c88108ac4998591c2a53fb01759c276c9ee661b20d31f67a375f3d31b0"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str = Field(min_length=8)
    role: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "user",
                "email": "user@gmail.com",
                "first_name": "John",
                "last_name": "Doe",
                "password": "password",
                "role": "user"
            }
        }
    }

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db # return
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def authenticate_user(db, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expire_delta: timedelta):
    encode = {
        "sub": username,
        "id": user_id
    }
    expires = datetime.now(timezone.utc) + expire_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_users(db: db_dependency):
    return db.query(Users).all()

@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      create_user_request: CreateUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True,
        role=create_user_request.role
    )

    db.add(create_user_model)
    db.commit()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = create_access_token(form_data.username, 1, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}