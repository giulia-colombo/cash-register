import unittest
from classes.inventory import Inventory
from classes.cash_register import CashRegister

class TestCashRegister(unittest.TestCase):
    def test_add_product(self):
        # purpose: successfully add item to cashregister.current_order
        # CASE 1: the product user wants to add doesn't exist
        # setup 1
        cash_register1 = CashRegister()
        initial_order1 = cash_register1.current_order.copy()
        # act 1
        cash_register1.add_product("Banana")
        # assert 1
        self.assertEqual(cash_register1.current_order, initial_order1)
        # CASE 2: an existing  product is added correctly to the current_order dictionary for the first time
        # setup 2:
        cash_register2 = CashRegister()
        # act 2
        cash_register2.add_product("Coffee")
        expected_current_order2 = {
            "Coffee": {
                "code": "CF1",
                "price": 11.23,
                "quantity": 1
            }
        }
        # assert 2
        self.assertEqual( cash_register2.current_order, expected_current_order2 )

        # CASE 3: an existing product is added correctly to the current_order dictionary for the 2nd or more time.
        # setup 3
        cash_register3 = CashRegister()
        cash_register3.current_order = {
            "Coffee": {
                "code": "CF1",
                "price": 11.23,
                "quantity": 1
            }
        }
        # act 3
        cash_register3.add_product("Coffee")
        expected_current_order3 = {
            "Coffee": {
                "code": "CF1",
                "price": 11.23,
                "quantity": 2
            }
        }
        # assert 3
        self.assertEqual(cash_register3.current_order, expected_current_order3)


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