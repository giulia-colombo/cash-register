import unittest
from classes.inventory import Inventory
from classes.cash_register import CashRegister

# TO DO: create_order method
# TO DO: pull prices dynamically from product catalog
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

    def test_apply_discount_greentea(self):
        # purpose: verify that the green tea discount is applied correctly (buy 1 get 1). So when the quantity of green tea is >= 2 and it's divisible by 2, the price becomes half.
        # setup
        green_tea_price = 3.11
        self.cash_register.current_order = {
            "green tea" : {
                "code": "GR1",
                "name": "Green Tea",
                "price": green_tea_price,
                "quantity": 4
            }
        }
        # act
        green_tea_discounted_value = self.cash_register.apply_discount_greentea()
        expected_green_tea_discounted_value = 6.22
        # assert
        self.assertEqual(green_tea_discounted_value, expected_green_tea_discounted_value)

    def test_apply_discount_coffee(self):
        # purpose: verify that the coffee discount is applied correctly.
        # If you buy 3 or more coffees, the price of all coffees should drop to 2/3 of the original price.
        # setup
        coffee_price = 11.23
        coffee_discount_coefficient = 0.66
        self.cash_register.current_order = {
        "coffee" : {
        "code": "CF1",
        "name": "Coffee",
        "price": coffee_price,
        "quantity": 4
    }
}
        # act
        coffee_discounted_value = self.cash_register.apply_discount_coffee()
        expected_coffee_discounted_value = coffee_price * coffee_discount_coefficient * self.cash_register.current_order["coffee"]["quantity"]
        # assert
        self.assertEqual(coffee_discounted_value, expected_coffee_discounted_value)



    def test_apply_discount_strawberries(self):
        # purpose: If you buy 3 or more strawberries, the price should drop to 4.50€.
        # setup
        strawb_full_price = 5.00
        strawb_discounted_price = 4.50

        self.cash_register.current_order = {
        "strawberries" : {
        "code": "SR1",
        "name": "Strawberries",
        "price": strawb_full_price,
        "quantity": 3
    }
}
        # act
        strawb_discounted_value = self.cash_register.apply_discount_strawberries()
        expected_strawb_discounted_value = self.cash_register.current_order["strawberries"]["quantity"] * strawb_discounted_price

        # assert
        self.assertEqual(strawb_discounted_value, expected_strawb_discounted_value)



    def test_calculate_total(self):
        # purpose: calculate and return the total value of products in the order
        # set up
        # act
        # assert
        pass

if __name__ == "__main__":
    unittest.main()