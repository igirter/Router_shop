from sqlalchemy.orm import Session
from models import User

def save_to_database(user: User, session: Session):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
