from typing import List
from products import Product
from factory import ShirtFactory, PantsFactory


class Inventory:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def calculate_total_price(self) -> float:
        total_price = 0.0
        for product in self.products:
            product.calculate_price()
            total_price += product.calculate_price()
        return total_price

