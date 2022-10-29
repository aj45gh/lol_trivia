import bcrypt
from sqlalchemy import select

from champions.database import db_session
from champions.models.user import User


def verify_login(username: str, password: str) -> bool:
    user = db_session.execute(
        select(User).where(User.username == username)
    ).first()

    if not user:
        return False

    print(user)
    return True


def add_user(username: str, password: str) -> bool:
    try:
        user = User(username=username, password=password)

        db_session.add(user)
        db_session.commit()

        return True
    except:
        return False
