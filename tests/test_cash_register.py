import unittest
from classes.inventory import Inventory
from classes.cash_register import CashRegister

class TestCashRegister(unittest.TestCase):
    def test_add_product(self):
        # create a CashRegister
        cash_reg = CashRegister()
        # create instance of Inventory
        # take the selected product (this supposes we are receiving the user input from another function, how do i do that here???) and check if it already exists in cash_reg.current_order
        # if it doesn't exist, add it to the current_order list
        # if it does exist, just increase the quantity in current_order
        pass

    def test_apply_discounts(self):
        pass

    def test_calculate_total(self):
        pass
