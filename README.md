# Student Management System (CLI → FastAPI + MySQL + JWT)

# 项目简介
这是一个基于 Python 实现的学生管理系统，最初为命令行（CLI）版本，后逐步升级为基于 FastAPI 的 Web 应用，并完成数据存储层从 JSON 文件到 MySQL 数据库的重构。

项目采用分层架构设计，支持学生信息的增删改查，引入JWT身份认证与基础权限控制，并具备良好的可扩展性与工程化结构。

系统特点：
- 支持 **CLI → Web API 演进**
- 数据存储由 **JSON 重构为 SQLite + SQLAlchemy ORM**
- 分离 **业务模型（Entity）与 API 模型（Pydantic Schema）**
- 项目采用分层架构设计（API / Service / DB / Models / Core），实现了学生信息管理、用户认证与基础权限控制，并具备较好的可扩展性与工程化设计能力。
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
- 异常处理 + 统一返回格式
- database url抽离

### 权限控制模块
- admin 用户可进行增删改操作
- 普通用户仅可查询数据

---

## 技术栈
- Python 3
- FastAPI
- SQLAlchemy（ORM）
- MySQL（数据存储）
- Pydantic（数据校验）
- 面向对象编程（OOP）
- 分层架构设计
- JWT
- bcrypt(密码加密)

---

## 项目结构

```text
Student_Manager/
├── .venv/                   
├── app/
│   ├── api/
│   │   ├── student_api.py    
│   │   └── user_api.py       
│   ├── core/
│   │   ├── config.py         
│   │   ├── jwt.py            
│   │   ├── logger.py         
│   │   ├── response.py       
│   │   └── security.py       
│   ├── db/
│   │   ├── crud.py          
│   │   └── session.py        
│   ├── models/
│   │   └── student.py        
│   ├── schemas/
│   │   ├── response_schema.py 
│   │   └── student_schema.py   
│   ├── service/              
│   └── .env                  
├── logs/                    
├── .gitignore                
├── main.py                   
├── README.md                 
├── students.db               
├── temp.py                 
└── test.html                 