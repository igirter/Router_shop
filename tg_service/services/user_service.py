from sqlalchemy.orm import Session

from database.models import TgUser
from database import repository

def get_user(
    tg_id: int,
    db: Session
):

    user = repository.get_user_by_tg_id(
        tg_id,
        db
    )

    return user

def create_user(
    tg_id: int,
    db: Session
):

    user = TgUser(
        tg_id=tg_id
    )

    user = repository.save_user(
        user,
        db
    )

    return user

def get_all_subscribers(db: Session):
    subscribers = repository.get_all_subscribers(db)

    return subscribers
