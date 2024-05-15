from pydantic import BaseModel

from .item import ItemResponse

class BaseUser(BaseModel):
  email: str

class UserCreateParam(BaseUser):
  password: str

class UserResponse(BaseUser):
  id: int
  items: list[ItemResponse] = []

  class Config:
    from_attributes = True
