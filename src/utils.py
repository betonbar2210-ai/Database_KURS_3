import json
import os

from config import ROOT_DIR
from src.airplane import Airplane


class JSONSaver():
    def __init__(self, filename: str = "airplanes.json"):
        self.filename = os.path.join(ROOT_DIR, "data", filename)
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    def clear_all(self) -> bool:
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return True

    def read_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_data(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_airplane(self, airplane: Airplane) -> None:
        data = self.read_data()
        data.append(airplane.to_dict())
        self.write_data(data)
