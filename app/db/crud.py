from app.models.student import Student, User
from sqlalchemy.orm import Session
import bcrypt


def create_student(db: Session, name: str, sex: str, age: int, s_id: str, score: int) -> Student:
    student = Student(name=name, sex=sex, age=age, s_id=s_id, score=score)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_student(db: Session, s_id: str):
    return db.query(Student).filter(Student.s_id == s_id).first()


def get_all(db: Session) -> list:
    return db.query(Student).all()


def delete_student(db: Session, s_id: str) -> bool:
    student = get_student(db, s_id)
    if not student:
        return False
    db.delete(student)
    db.commit()
    return True


def update_student(db: Session, student_id: str, **kwargs) -> Student:
    """
    kwargs: 只包含需要更新的字段
    自动过滤 None，未传字段不会被覆盖
    """
    student = get_student(db, student_id)
    if not student:
        raise Exception("Student not found")
    for key, value in kwargs.items():
        if value is not None:
            setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return student


def create_user(db: Session, username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = User(username=username, password=hashed_password.decode('utf-8'))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    return user


def verify_user(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

