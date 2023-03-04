import os
from dotenv import load_dotenv
from typing import Any


class Config:
    def __init__(self, filename: str):
        load_dotenv(filename)

    @staticmethod
    def get(key: str, default: Any = None) -> Any:
        return os.environ.get(key, default)


config = Config('.env')