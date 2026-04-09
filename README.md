# Student Management System (CLI → FastAPI + SQLite)

## 项目简介
这是一个基于 Python 实现的学生管理系统，最初为命令行（CLI）版本，后逐步升级为基于 FastAPI 的 Web 应用，并完成数据存储层从 JSON 文件到 SQLite 数据库的重构。

项目采用分层架构设计，支持学生信息的增删改查，并具备良好的可扩展性与工程化结构。

系统特点：
- 支持 **CLI → Web API 演进**
- 数据存储由 **JSON 重构为 SQLite + SQLAlchemy ORM**
- 分离 **业务模型（Entity）与 API 模型（Pydantic Schema）**
- 分层架构（API / Service / Repository / Database）
- 支持日志记录与错误追踪

---

## 功能

### CLI 版本（早期）
- 添加学生
- 查看所有学生
- 根据学号查找学生
- 修改学生信息
- 删除学生

### FastAPI 版本（当前）
- 提供 RESTful API 接口
- 自动生成接口文档（/docs）
- 数据校验（Pydantic）
- 学生信息增删改查（CRUD）
- 分层架构解耦业务逻辑
- 支持扩展分页 / 搜索

---

## 技术栈
- Python 3
- FastAPI
- SQLAlchemy（ORM）
- SQLite（当前数据存储）
- Pydantic（数据校验）
- 面向对象编程（OOP）
- 分层架构设计

---

## 项目结构

```text
Student_Manager/
├── app/
│   ├── api/                # 接口层（FastAPI 路由）
│   │   └── student_api.py
│   ├── handlers/           # CLI遗留逻辑（逐步废弃）
│   └── logs/               # 日志目录
│
├── database/               # 数据库层（核心升级）
│   ├── crud.py             # 数据库操作（CRUD）
│   ├── db_core.py          # 数据库连接管理（engine / Session）
│   └── models.py           # ORM模型定义
│
├── model/                  # 数据模型层
│   ├── student.py          # 业务实体（Entity）
│   └── student_schema.py   # API模型（Pydantic）
│
├── service/                # 业务逻辑层
│   └── student_service.py
│
├── repository/             # 旧版数据访问层（JSON版本遗留）
│
├── data/                   # JSON数据（已废弃）
│   └── students.json
│
├── logs/                   # 全局日志
│
├── students.db             # SQLite数据库
├── main.py                 # 启动入口
└── README.md