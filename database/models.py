from sqlalchemy import Column, Integer, String
from database.db_core import Base


class Student(Base):
    __tablename__ = 'student'
    name = Column(String, index=True)
    sex = Column(String)
    age = Column(Integer)
    s_id = Column(String, primary_key=True, index=True)
    score = Column(Integer)
