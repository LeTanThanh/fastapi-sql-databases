from sqlalchemy.orm import Session

from orms.user import User

def get_users_by_offset_and_limit(session: Session, offset: int = 0, limit: int = 100) -> list[User]:
  return session.query(User).offset(offset).limit(limit).all()
