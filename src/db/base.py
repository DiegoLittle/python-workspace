from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
if not os.path.exists(SQLALCHEMY_DATABASE_URL.replace("sqlite:///", "")):
    with open(SQLALCHEMY_DATABASE_URL.replace("sqlite:///", ""), "w") as f:
        f.write("")
metadata_obj = MetaData()


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base(metadata=metadata_obj)
