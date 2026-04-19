from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


PATH = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(
    PATH,
    echo=True
)

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
