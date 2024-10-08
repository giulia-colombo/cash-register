import unittest
from classes.inventory import Inventory

class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()

    def test_retrieve_product(self):
        
        product = self.inventory.retrieve_product("coffee")
        expected_product = {
                "code": "CF1",
                "name": "Coffee",
                "price": 11.23
            }

        self.assertEqual(product, expected_product)

        product = self.inventory.retrieve_product("green tea")
        expected_product = {
                "code": "GR1",
                "name": "Green Tea",
                "price": 3.11
            }
    
        self.assertEqual(product, expected_product)        

        product = self.inventory.retrieve_product("strawberries")
        expected_product =  {
                "code": "SR1",
                "name": "Strawberries",
                "price": 5
            }
    
        self.assertEqual(product, expected_product)  

        product = self.inventory.retrieve_product("Banana")
        self.assertIsNone(product)

if __name__ == "__main__":
    unittest.main()