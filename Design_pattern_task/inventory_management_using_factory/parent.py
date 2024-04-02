from typing import Optional
from factory import AbstractFactory, ShirtFactory, PantsFactory


class ProductFactory:
    def __new__(cls, product_type: str) -> Optional[AbstractFactory]:
        if product_type == "shirt":
            return ShirtFactory()
        elif product_type == "pant":
            return PantsFactory()
