from sqlalchemy import select
from api.config.database import session
from api.helpers.model_serializer import Serializer
from api.models.item import Item

def search_items_service():
    rows = session.query(Item).all()
    return Serializer.serialize_list(rows)

def get_item_service(id):
    # 2 different ways to do the same
    # item = session.query(Item).filter(Item.id==id).one()
    item = session.query(Item).get(id)
    return item.serialize()

def create_item_service(name, description):
    session.add(Item(name=name, description=description))
    session.commit()

def update_item_service(id, name, description):
    session.query(Item).filter_by(id=id).update(
        dict(name=name, description=description)
    )
    session.commit()

def delete_item_service(id):
    session.query(Item).filter_by(id=id).delete()
    session.commit()