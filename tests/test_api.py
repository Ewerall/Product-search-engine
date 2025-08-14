import requests
import pytest

from app.product import Product


@pytest.mark.parametrize("category", {
    "electronics",
    "clothes",
    "shoes",
    "home"
})
def test_category(category: str):
    response = requests.get(f"http://localhost:8000/products?category={category}")

    assert response.status_code == 200, f"API вернул ошибку для категории {category}"
    assert response.headers["Content-Type"] == "application/json", "Ответ не в JSON"

    products = [Product.from_json(item) for item in response.json()]

    assert len(products) > 0, f"Нет товаров в категории {category}"

    assert all(p.category == category for p in products), (
        f"Не все товары в категории {category} соответствуют запросу"
    )
