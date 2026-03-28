Student Management System (Python CLI)
项目简介
一个基于 Python 实现的命令行学生管理系统，支持学生信息的增删改查，并使用 JSON 文件实现数据持久化。
功能:
    添加学生
    查看所有学生
    根据学号查找学生
    修改学生信息
    删除学生
技术栈:
    Python 3
    面向对象编程（OOP）
    JSON 数据存储
    分层设计（handler / service / utils）
项目结构:
    app/        程序入口  
    handlers/   交互逻辑  
    service/    业务逻辑  
    model/      数据模型  
    utils/      工具类（文件处理）  
    data/       数据存储  
使用分层架构，降低模块耦合
将文件操作抽离到 utils 层，实现业务与存储解耦
支持数据持久化（JSON）

运行方式:
    python app/main.py
后续优化:
    使用 SQLite 替代 JSON
    增加日志系统
    提供 Web 接口（FastAPI）