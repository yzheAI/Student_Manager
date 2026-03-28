import os
import json
from utils.log_util import logger
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'students.json')


def load_data() -> list[dict]:
    if not os.path.exists(DATA_PATH):
        return []

    with open(DATA_PATH, 'r', encoding='utf8') as f:
        return json.load(f)  # 返回所有信息


def save_data(data) -> None:
    try:
        with open(DATA_PATH, 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logger.info("Data saved successfully")
    except Exception as e:
        logger.error(f"Data save failed due to {e}")
