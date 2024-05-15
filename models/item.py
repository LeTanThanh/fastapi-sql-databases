from pydantic import BaseModel

class BaseItem(BaseModel):
  title: str
  description: str

class ItemCreateParam(BaseItem):
  pass

class ItemResponse(BaseItem):
  id: int
  owner_id: int

  class Config:
    from_attributes = True
