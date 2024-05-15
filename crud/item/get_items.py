from sqlalchemy.orm import Session

from orms.item import Item

def get_items_by_offset_and_limit(session: Session, offset: int = 0, limit: int = 100) -> list[Item]:
  return session.query(Item).offset(offset).limit(limit).all()
