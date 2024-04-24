from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_tax_amount(self) -> float:
        pass

    @abstractmethod
    def get_raw_materials(self) -> str:
        pass

    def calculate_price(self) -> float:
        return self.get_price() + self.get_tax_amount()


class Shirt(Product):
    def get_price(self) -> float:
        return 20.0

    def get_tax_amount(self) -> float:
        return 10.0

    def get_raw_materials(self) -> str:
        return "Bangladesh"

class Pants(Product):
    def get_price(self) -> float:
        return 30.0

    def get_tax_amount(self) -> float:
        return 0.0

    def get_raw_materials(self) -> str:
        return "China"
