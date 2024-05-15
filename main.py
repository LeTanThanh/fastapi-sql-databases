from fastapi import Depends, FastAPI, HTTPException, Path
from sqlalchemy.orm import Session

from orms.item import Item
from orms.user import User

from models.user import UserResponse
from models.user import UserCreateParam

from crud.user.get_users import get_users_by_offset_and_limit
from crud.user.get_user import get_user_by_id
from crud.user.get_user import get_user_by_email
from crud.user.create_user import create_user as crud_create_user

from depends.database.session import get_session

from database import SessionLocal
from database import engine
from database import BaseORM

from typing import Annotated

BaseORM.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users", response_model = UserResponse)
async def create_user(user: UserCreateParam, session: Session = Depends(get_session)) -> UserResponse:
  orm_user = get_user_by_email(session = session, email = user.email)

  if orm_user:
    raise HTTPException(
      status_code = 400,
      detail = "Email already registered"
    )

  return crud_create_user(session = session, user = user)

@app.get("/users", response_model=list[UserResponse])
async def read_users(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)) -> list[UserResponse]:
  orm_users = get_users_by_offset_and_limit(session = session, offset = offset, limit = limit)
  return orm_users

@app.get("/users/{id}", response_model = UserResponse)
async def read_user(id: Annotated[int, Path()], session: Session = Depends(get_session)) -> UserResponse:
  orm_user = get_user_by_id(session = session, id = id)
  if orm_user is None:
    raise HTTPException(status_code=404, detail="User not found")

  return orm_user
