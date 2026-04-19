from sqlalchemy import Column, Integer, String
from app.db.session import Base


class Student(Base):
    __tablename__ = 'student'
    name = Column(String(20), index=True)
    sex = Column(String(20))
    age = Column(Integer)
    s_id = Column(String(255), primary_key=True, index=True)
    score = Column(Integer)


class User(Base):
    __tablename__ = 'user'
    username = Column(String(50), primary_key=True, index=True)
    password = Column(String(255))
    role = Column(String(50), default="user")
