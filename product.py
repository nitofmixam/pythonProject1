from category import Category


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name  # название товара (строка)
        self.description = description  # описание товара (строка)
        self.price = price  # цена товара (float, например, 99.99)
        self.quantity = quantity  # количество товара в наличии (целое число)
        Category.total_categories += 1
