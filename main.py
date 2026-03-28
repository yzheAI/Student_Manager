from service.student_service import StudentManager
from app.handlers.handle_add import handle_add_student
from app.handlers.handle_show import show
from app.handlers.handle_find import find_student_id
from app.handlers.handle_delete import handle_delete_student
from app.handlers.handle_update import handle_update_student
from repository.student_repo import StudentRepository
repo = StudentRepository("data/students.json")
manager = StudentManager(repo)


def menu() -> None:
    while True:
        print("1. 添加学生\n2. 查看所有学生\n3. 查找学生\n4. 修改学生\n5. 删除学生\n6. 退出")
        try:
            choose = int(input("请输入要进行的操作编号："))
        except ValueError:
            print("请输入数字")
            return None

        if choose == 1:
            handle_add_student(manager)
        elif choose == 2:
            show(manager)
        elif choose == 3:
            find_student_id(manager)
        elif choose == 4:
            handle_update_student(manager)
        elif choose == 5:
            handle_delete_student(manager)
        else:
            break


menu()
