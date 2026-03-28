from typing import List
from model.student import Student
from utils.log_util import logger


class StudentManager:
    def __init__(self, repo):
        self.repo = repo
        self.students: List[Student] = self.repo.load()

    def add_student(self, student: Student) -> None:
        if self.find_student(student.student_id):
            print("学号重复，拒绝添加！")
            return
        self.students.append(student)
        logger.info(f"新增学生: {student.name}, 学号: {student.student_id}")
        self.save_to_file()
        print("添加成功")

    def show_all(self) -> None:
        if self.students is None:
            print("暂无学生")
            return
        for s in self.students:
            print(s.to_dict())

    def find_student(self, student_id: str) -> Student | None:
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def update_student(self, student: Student) -> None:
        # self.load_from_file()
        s = self.find_student(student.student_id)
        if s is None:
            print("无信息")
            return None
        else:
            s.name = student.name
            s.sex = student.sex
            s.age = student.age
            s.score = student.score
            self.save_to_file()
        print("修改成功")

    def delete_student(self, student_id: str) -> None:
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            self.save_to_file()
            logger.info(f"删除学生: {student_id}")
            print("删除成功")
        else:
            print("不存在")

    def save_to_file(self) -> None:
        self.repo.save(self.students)

