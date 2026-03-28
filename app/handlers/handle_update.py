from model.student import Student



def handle_update_student(manager) -> None:
    student_id = input("请输入要修改的学生学号：")
    name = input("请输入姓名")
    sex = input("请输入性别")
    try:
        age = int(input("请输入年龄"))
        score = int(input("请输入成绩"))
    except ValueError:
        print("请输入数字！")
        return

    student = Student(name, sex, age, student_id, score)
    manager.update_student(student)
