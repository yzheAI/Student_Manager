# Student Management System (Python CLI & FastAPI)

## 项目简介
这是一个基于 Python 实现的学生管理系统，最初为命令行（CLI）版本，后升级为支持 **FastAPI** 的 Web 接口。系统采用分层架构设计，支持学生信息的增删改查，并实现数据持久化。

系统特点：
- 分离 **业务模型**（Student 类）与 **API 模型**（Pydantic Schema），提高代码可维护性与可扩展性
- 使用 JSON 文件存储数据（未来可升级为数据库）
- 支持日志记录操作
- 面向对象设计，业务与存储解耦

---

## 功能

### CLI 版本
- 添加学生
- 查看所有学生
- 根据学号查找学生
- 修改学生信息
- 删除学生

### FastAPI 版本
- 提供 RESTful API 接口
- 数据校验（Pydantic 模型）
- 支持学生信息的增删改查
- 分离接口与业务逻辑
- 支持分页和搜索（可扩展）

---

## 技术栈
- Python 3
- 面向对象编程（OOP）
- FastAPI + Pydantic（Web 接口）
- JSON 数据存储
- 分层设计（API / Service / Repository / Model / Utils）

---

## 项目结构

```text
student_management_system/
├── app/                # 程序入口
│   └── main.py
├── api/                # FastAPI 路由
│   └── student_api.py
├── handlers/           # CLI 交互逻辑
├── service/            # 业务逻辑
│   └── student_service.py
├── repository/         # 数据持久化
│   └── student_repo.py
├── model/              # 数据模型
│   ├── student.py          # Entity 模型
│   ├── student_schema.py   # API 模型（Pydantic Schema）
│   └── converter.py        # Entity ↔ Schema 转换
├── utils/              # 工具类（文件处理、日志）
├── data/               # JSON 数据存储
├── logs/               # 日志文件夹
└── README.md           # 项目说明