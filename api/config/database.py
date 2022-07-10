from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os

from api.helpers.model_serializer import Serializer

# For development purposes
DEFAULT_CONNECTION_STRING = "sqlite+pysqlite:///:memory:?check_same_thread=False"

def get_connection_string():
    env_str = os.getenv('DATABASE_URL')
    if env_str is not None:
        return env_str
    return DEFAULT_CONNECTION_STRING        

engine = create_engine(get_connection_string(), echo=True, future=True)

session = Session(engine, future=True)

