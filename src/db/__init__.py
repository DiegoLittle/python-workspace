import os
from uuid import uuid4
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from db.base import Base

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")


def get_uuid():
    return str(uuid4())


def initalize_db():
    from db.models.Dummy import DummyModel

    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})
    Base.metadata.create_all(bind=engine)
