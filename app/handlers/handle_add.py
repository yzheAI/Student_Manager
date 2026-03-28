from model.student import Student


def handle_add_student(manager) -> None:
    name = input("请输入姓名： ")
    sex = input("请输入性别： ")
    try:
        age = int(input("请输入年龄： "))
        score = int(input("请输入成绩： "))
    except ValueError:
        print("请输入数字！")
        return
    student_id: str = input("请输入学号： ")
    student = Student(name, sex, age, student_id, score)
    manager.add_student(student)


