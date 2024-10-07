import unittest
from classes.inventory import Inventory
from classes.product import Product

class InventoryTest(unittest.TestCase):
    def test_retrieve_product(self):
        inventory = Inventory()
        product = inventory.retrieve_product("Coffee")
        expected_product = Product("CF1", "Coffee", 11.23)
        self.assertEqual(product, expected_product)
        product = inventory.retrieve_product("Banana")
        self.assertIsNone(product)

if __name__ == "__main__":
    unittest.main()