import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)  # 创建文件夹logs

LOG_PATH = os.path.join(LOG_DIR, "app.log")  # 日志文件路径

logging.basicConfig(  # 初始化
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[  # 日志输出到哪里
        logging.FileHandler(LOG_PATH, encoding="utf-8"),  # 日志写入
    ]
)

logger = logging.getLogger()  # 获取全局日志对象，可以用logger.info()
