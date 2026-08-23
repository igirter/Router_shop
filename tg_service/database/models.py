from sqlalchemy import Column, Integer, Boolean
from db import Base

class TgUser(Base):
    __tablename__ = "telegram_users"

    tg_id = Column(Integer, primary_key=True, unique=True, nullable=False, index=True)
    subscribed = Column(Boolean, default=True)
