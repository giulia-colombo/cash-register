import unittest
from classes.inventory import Inventory
from classes.cash_register import CashRegister

class TestCashRegister(unittest.TestCase):
    def setUp(self):
        self.cash_register = CashRegister()
        self.inventory = Inventory()
        self.products = self.inventory.product_catalog

    def test_add_product(self):
        # purpose: successfully add item to cashregister.current_order

        # CASE 1: the product user wants to add doesn't exist
        initial_order = self.cash_register.current_order.copy()
        self.cash_register.add_product("banana")
        self.assertEqual(self.cash_register.current_order, initial_order)

        # CASE 2: an existing  product is added correctly to the current_order dictionary for the first time
        expected_current_order = {}
        for product_name, product_info in self.products.items():
            self.cash_register.add_product(product_name)

            expected_current_order[product_name] = {
                "code": product_info["code"],
                "name": product_info["name"],
                "price": product_info["price"],
                "quantity": 1
            }
            self.assertEqual( self.cash_register.current_order, expected_current_order )

        # CASE 3: an existing product is added correctly to the current_order dictionary for the 2nd or more time.
        # act 3
        self.cash_register.add_product("coffee")
        expected_current_order["coffee"]["quantity"] +=1
        # assert 3
        self.assertEqual(self.cash_register.current_order, expected_current_order)


    def test_apply_discount_coffee(self):
        pass

    def test_apply_discount_greentea(self):
        pass

    def test_apply_discount_strawberries(self):
        pass


    def test_calculate_total(self):
        pass

if __name__ == "__main__":
    unittest.main()