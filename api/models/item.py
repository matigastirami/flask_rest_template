from sqlalchemy import Column, Integer, String
from api.config.database import engine
from api.models.base import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

Base.metadata.create_all(engine)