from sqlalchemy.orm import Session

from orms.user import User
from models.user import UserCreateParam

def create_user(session: Session, user: UserCreateParam) -> User:
  hashed_password = user.password + "notreallyhashed"
  orm_user = User(email = user.email, hashed_password = hashed_password)
  session.add(orm_user)
  session.commit()
  session.refresh(orm_user)
  return orm_user
