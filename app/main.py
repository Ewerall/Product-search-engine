"""Основные API запросы"""
import os

from dataclasses import asdict
from fastapi import FastAPI

from app.utils import load_from_json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_PATH = os.path.join(BASE_DIR, "..", "products.json")

app = FastAPI()

products = load_from_json(PRODUCTS_PATH)


@app.get("/products")
def get_products(category: str = None, tags: str = None):  # type: ignore
    """Выдаем товары в заданной категории или с тэгом"""
    filtered = products

    if category:
        filtered = [p for p in filtered if category == p.category]

    if tags:
        filtered = [p for p in filtered if tags in p.tags]

    return [asdict(p) for p in filtered]


@app.get("/search")
def search_product(s: str):
    """Ищем по строку в названии или описании товара и выдаем все совпавшие"""
    s = s.lower()
    results = [
        p for p in products
        if s in p.name.lower() or s in p.description.lower()
    ]
    return [asdict(p) for p in results]
