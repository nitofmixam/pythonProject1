import pytest
from category import Category
from product import Product


# Тестирование инициализации объектов класса Category
def test_category_initialization():
    category = Category("Электроника", "Категория электронных устройств")
    assert category.name == "Электроника"
    assert category.description == "Категория электронных устройств"


# Тестирование инициализации объектов класса Product
def test_product_initialization():
    product = Product("Ноутбук", "Высокопроизводительный ноутбук", 999.99, 10)
    assert product.name == "Ноутбук"
    assert product.description == "Высокопроизводительный ноутбук"
    assert product.price == 999.99
    assert product.quantity == 10


# Подсчет количества категорий
def test_category_count():
    electronics_category = Category("Электроника", "Категория электронных устройств")
    clothing_category = Category("Одежда", "Категория для одежды")

    assert len([electronics_category, clothing_category]) == 2


# Запуск тестов
if __name__ == '__main__':
    pytest.main()
