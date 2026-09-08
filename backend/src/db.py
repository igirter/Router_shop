from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os
from typing import cast

load_dotenv()
DATABASE = cast(str, os.getenv("DATABASE_BACKEND"))

engine = create_engine(DATABASE)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
