"""Классы для работы с продуктами"""

from dataclasses import dataclass

from typing import List, Dict, Any


@dataclass  # Используем Dataclass потому, что быстрее
class Product:
    """Базовый класс Product для хранения данных"""
    id: int
    name: str
    price: int
    category: str
    brand: str
    rating: float
    stock: int
    is_available: bool
    tags: List[str]
    description: str

    @classmethod
    def from_json(cls, data: Dict[str, Any]):
        """Преобразует JSON-словарь в объект Product"""
        return cls(
            id=data["id"],
            name=data["name"],
            price=data["price"],
            category=data["category"],
            brand=data["brand"],
            rating=data["rating"],
            stock=data["stock"],
            is_available=data["is_available"],
            tags=data["tags"],
            description=data["description"])
