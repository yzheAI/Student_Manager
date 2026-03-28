def find_student_id(manager) -> None:
    id_find = input("请输入学号： ")
    s = manager.find_student(id_find)
    if s is None:
        print("不存在")
    else:
        s.show()
