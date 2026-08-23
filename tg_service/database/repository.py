from sqlalchemy.orm import Session

from models import TgUser

def get_user_by_tg_id(
    tg_id: int,
    db: Session
):

    user = db.query(TgUser).filter(TgUser.tg_id == tg_id).first()

    return user


def get_all_subscribers(db: Session):
    users = db.query(TgUser).filter(
        TgUser.subscribed == True
    ).all()

    return users

def get_all_users(db: Session):
    users = db.query(TgUser).all()

    return users

def save_user(user: TgUser, db: Session):
    db.add(user)
    db.commit()
    db.refresh()

    return user
