from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship

from database import BaseORM

class User(BaseORM):
  __tablename__ = "users"

  id = Column(Integer, primary_key = True)
  email = Column(String, unique = True, index = True)
  hashed_password = Column(String)
  is_active = Column(Boolean, default = True)

  items = relationship("Item", back_populates = "owner")
