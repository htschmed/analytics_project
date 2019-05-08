import os
from .property import Property
from .modiv import MODIV
from .sr1a import SR1A
from . import Base
from sqlalchemy import create_engine


def get_engine():
    db_name = os.getenv('POSTGRES_DB')
    db_user = os.getenv('POSTGRES_USER')
    db_password = os.getenv('POSTGRES_PASSWORD')
    db_host = os.getenv('POSTGRES_HOST')
    conn_string = 'postgresql+psycopg2://{}:{}@{}/{}'
    engine = create_engine(conn_string.format(
        db_user, db_password, db_host, db_name
    ))
    return engine


def create_database():
    engine = get_engine()
    Base.metadata.create_all(engine)
