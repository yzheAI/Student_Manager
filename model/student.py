class Person:
    def __init__(self, name, sex, age):
        self.name: str = name
        self.sex: str = sex
        self.age: int = age

    def show(self) -> None:
        print(f"姓名{self.name},性别{self.sex},年龄{self.age}")


class Student(Person):
    def __init__(self, name, sex, age, student_id, score):
        super().__init__(name, sex, age)
        self.student_id: str = student_id
        self.score = score

    def to_dict(self) -> dict:  # return dict
        return {
            "name": self.name,  # dict type
            "sex": self.sex,
            "age": self.age,
            "student_id": self.student_id,
            "score": self.score
        }

    @staticmethod
    def from_dict(data) -> "Student":  # class is not defined
        return Student(
            data['name'],
            data['sex'],
            data['age'],
            data['student_id'],
            data['score']
        )

    def show(self) -> None:
        print(f"姓名{self.name}, 性别{self.sex}, 年龄{self.age}, 学号{self.student_id}, 成绩{self.score}")


class Teacher(Person):
    def __init__(self, name, sex, age, teacher_id, position, course):
        super().__init__(name, sex, age)
        self.teacher_id: str = teacher_id
        self.position: str = position
        self.course: int = course

    def show(self) -> None:
        print(
            f"姓名{self.name}, 性别{self.sex}, 年龄{self.age}, 职工号{self.teacher_id}, 职位{self.position}, 教授课程{self.course}")

