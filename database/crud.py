from database.models import Student
from sqlalchemy.orm import Session


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


def update_student(db: Session, student_id: str, name=None, age=None, sex=None, score=None) -> Student:
    student = get_student(db, student_id)
    if not student:
        raise Exception("Student not found")
    if name is not None:
        student.name = name
    if sex is not None:
        student.sex = sex
    if age is not None:
        student.age = age
    if score is not None:
        student.score = score
    db.commit()
    db.refresh(student)
    return student
