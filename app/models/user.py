from app.db.session import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'user'
    username = Column(String(50), primary_key=True, index=True)
    password = Column(String(255))
    role = Column(String(50), default="user")
