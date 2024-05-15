from pydantic import BaseModel

from item import ItemResponse

class BaseUser(BaseModel):
  email: str

class UserCreateParam(BaseUser):
  password: str

class User(BaseUser):
  id: int
  owner_id: int
  items: list[ItemResponse] = []

  class Config:
    orm_mode = True
