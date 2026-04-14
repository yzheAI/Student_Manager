# Student Management System (CLI → FastAPI + SQLite + JWT)

# 项目简介
这是一个基于 Python 实现的学生管理系统，最初为命令行（CLI）版本，后逐步升级为基于 FastAPI 的 Web 应用，并完成数据存储层从 JSON 文件到 SQLite 数据库的重构。

项目采用分层架构设计，支持学生信息的增删改查，引入JWT身份认证与基础权限控制，并具备良好的可扩展性与工程化结构。

系统特点：
- 支持 **CLI → Web API 演进**
- 数据存储由 **JSON 重构为 SQLite + SQLAlchemy ORM**
- 分离 **业务模型（Entity）与 API 模型（Pydantic Schema）**
- 分层架构（API / Service / Repository / Database）
- 支持日志记录与错误追踪
- 实现 JWT 用户认证与基础 RBAC 权限控制

---

## 功能

### CLI 版本（早期）
- 添加学生
- 查看所有学生
- 根据学号查找学生
- 修改学生信息
- 删除学生

### FastAPI 版本
- 提供 RESTful API 接口
- 自动生成接口文档（/docs）
- 数据校验（Pydantic）
- 学生信息增删改查（CRUD）
- 分层架构解耦业务逻辑
- 登录注册JWT

### 权限控制模块
- admin 用户可进行增删改操作
- 普通用户仅可查询数据

---

## 技术栈
- Python 3
- FastAPI
- SQLAlchemy（ORM）
- SQLite（当前数据存储）
- Pydantic（数据校验）
- 面向对象编程（OOP）
- 分层架构设计
- JWT
- bcrypt(密码加密)

---

## 项目结构

```text
Student_Manager/
├── app/
│   ├── api/                # 路由层（Controller）
│   │   ├── student_api.py
│   │   └── user_api.py
│   ├── handlers/           # CLI遗留逻辑（逐步废弃）
│   └── logs/
│
├── database/
│   ├── crud.py             # 数据库操作层（DAO）
│   ├── db_core.py          # 数据库连接管理
│   └── models.py           # ORM模型定义
│
├── model/
│   ├── student.py          # 业务实体层
│   └── student_schema.py   # Pydantic 数据校验层
│
├── service/                # 业务逻辑层（可扩展）
│
├── repository/             # JSON版本遗留（历史结构）
│
├── utils/
│   ├── jwt_utils.py        # JWT工具类
│   ├── security.py         # 鉴权逻辑
│   └── response.py         # 统一返回封装
│
├── data/
│   └── students.json       # 旧数据存储（已废弃）
│
├── logs/
├── students.db
├── main.py
└── README.md
