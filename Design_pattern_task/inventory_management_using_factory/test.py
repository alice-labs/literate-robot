from parent import ProductFactory
from inventory import Inventory
import unittest


class TestDocumentEditor(unittest.TestCase):
    def setUp(self):
        self.shirt_factory = ProductFactory("shirt")
        self.pants_factory = ProductFactory("pant")
        self.inventory = Inventory()

    def test_product(self):
        self.inventory.add_product(self.shirt_factory.create_product())
        self.inventory.add_product(self.pants_factory.create_product())
        self.inventory.add_product(self.pants_factory.create_product())
        self.assertEqual(self.inventory.calculate_total_price(), 90.0)


if __name__ == "__main__":
    unittest.main()
