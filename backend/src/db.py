from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE = "sqlite:///users.db"

engine = create_engine(DATABASE)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
