import json

from typing import List

from app.product import Product


def load_from_json(file_path: str) -> List[Product]:
    """Загружаем json и создаем список обьектов из него"""
    with open(file_path, 'r', encoding="utf-8") as js:
        data = json.load(js)
    return [Product.from_json(item) for item in data]  # list comprehension aka генератор списков
