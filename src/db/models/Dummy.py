import json
from sqlalchemy import Column, String
from db import get_uuid
from db.base import Base
from db.utils import isJsonDeserializable


class DummyModel(Base):
    __tablename__ = "dummy"
    id = Column(String, primary_key=True, index=True, default=get_uuid)
    title = Column(String, index=True)
    description = Column(String, index=True)
    meta_data = Column(String, index=True)
