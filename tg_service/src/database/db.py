from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
from typing import cast

load_dotenv()

DATABASE = cast(str, os.getenv("DATABASE"))

engine = create_engine(DATABASE)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()



def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
