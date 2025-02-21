from fastapi import APIRouter, Depends, HTTPException, Path
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from models import Todos
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user

router = APIRouter(prefix="/todos", tags=["todos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new todo",
                "description": "A description of a todo",
                "priority": 1,
                "complete": False
            }
        }
    }

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    complete: bool

    class Config:
        from_attributes = True

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_todos(db: db_dependency):
    return db.query(Todos).all()

@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return TodoResponse.model_validate(todo_model)
    raise HTTPException(status_code=404, detail='Todo not found.')

@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency, db: db_dependency, todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Unauthorized')

    try:
        todo_model = Todos(**todo_request.model_dump(), owner_id=user.get('id'))

        db.add(todo_model)
        db.commit()
        db.refresh(todo_model)

        return TodoResponse.model_validate(todo_model)

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating todo: {str(e)}")


@router.put("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user: user_dependency, db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Unauthorized')

    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')

    if todo_model.owner_id != user.get('id'):
        raise HTTPException(status_code=403, detail="You are not authorized to update this todo.")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    # db.add(todo_model)
    db.commit()

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')

    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()