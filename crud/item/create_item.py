from sqlalchemy.orm import Session

from orms.item import Item
from models.item import ItemCreateParam

def create_user_item(session: Session, item: ItemCreateParam, user_id: int) -> Item:
  orm_item = Item(**item.model_dump(exclude_unset = True), owner_id = user_id)
  session.add(orm_item)
  session.commit()
  session.refresh(orm_item)
  return orm_item
