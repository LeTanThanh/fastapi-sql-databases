from sqlalchemy.orm import Session

from orms.user import User

def get_user_by_id(session: Session, id: int) -> User | None:
  return session.query(User).filter(User.id == id).first()

def get_user_by_email(session: Session, email: str) -> User | None:
  return session.query(User).filter(User.email == email).first()
