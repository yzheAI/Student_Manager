from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

PATH = "sqlite:///students.db"
engine = create_engine(
    PATH,
    # SQLite特有，多线程访问
    connect_args={"check_same_thread": False})

# 创建Session工厂，每次操作从这里拿连接
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
# 所有 ORM 模型的父类
# Student类 继承这个Base
Base = declarative_base()


# 数据库资源管理器
def get_db():
    # 一次数据库连接
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
