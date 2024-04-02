from abc import ABC, abstractmethod
from products import Product, Shirt, Pants


class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self) -> Product:
        pass

class ShirtFactory(AbstractFactory):
    def create_product(self) -> Product:
        return Shirt()

class PantsFactory(AbstractFactory):
    def create_product(self) -> Product:
        return Pants()

