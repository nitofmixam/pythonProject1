class Category:
    name: str
    description: str
    products: list
    category_count = 0
    total_categories = 0

    def __init__(self, name, description):
        self.name = name  # название категории (строка)
        self.description = description  # описание категории (строка)
        self.products = []  # список товаров в данной категории
        Category.total_categories += 1