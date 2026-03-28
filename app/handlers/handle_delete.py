

def handle_delete_student(manager) -> None:
    student_id = input("请输入学号：")
    manager.delete_student(student_id)
