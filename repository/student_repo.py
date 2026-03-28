from typing import List
from model.student import Student
import json
import os


class StudentRepository:
    def __init__(self, file_path: str):  # 创建仓库，不指定路径
        self.file_path = file_path

    def load(self) -> List[Student]:  # 返回列表
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Student.from_dict(d) for d in data]

    def save(self, students: List[Student]) -> None:
        data = [s.to_dict() for s in students]
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
