from sqlalchemy import Column, Integer
from db import Base

class TgUser(Base):
    __tablename__ = "telegram_users"

    id = Column(Integer, primary_key=True, index=True)
    tg_id = Column(Integer, unique=True, nullable=False, index=True)
