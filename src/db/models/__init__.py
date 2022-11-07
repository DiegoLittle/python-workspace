from . import Dummy
from db.base import Base, engine

Base.metadata.create_all(bind=engine)
