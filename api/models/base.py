from sqlalchemy.orm import registry
from sqlalchemy.orm.decl_api import DeclarativeMeta

from api.helpers.model_serializer import Serializer

mapper_registry = registry()

class Base(metaclass=DeclarativeMeta):
    __abstract__ = True
    registry = mapper_registry
    metadata = mapper_registry.metadata
    __init__ = mapper_registry.constructor

    def serialize(self):
        d = Serializer.serialize(self)
        return d