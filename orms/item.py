from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import BaseORM

class Item(BaseORM):
  __tablename__ = "items"

  id = Column(Integer, primary_key = True)
  title = Column(String, index = True)
  description = Column(String, index = True)
  owner_id = Column(Integer, ForeignKey("users.id"))

  owner = relationship("User", back_populates = "items")
