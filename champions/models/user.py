from sqlalchemy import Column, Integer, String

from champions.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        # TODO: Hash password before saving
